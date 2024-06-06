# ACCELDATA-AIRFLOW-SDK

Acceldata airflow sdk provides support for observability of airflow dags in torch catalog. With the use of acceldata airflow SDK, user can e2e observability on airflow dag run in torch UI. Every dag is associated with pipeline in torch.
<br />
Make sure while configuring airflow, 4 environment variable are set up in airflow environment docker container.


* TORCH_CATALOG_URL - URL of the torch catalog
* TORCH_ACCESS_KEY - API access key generated from torch UI
* TORCH_SECRET_KEY - API secret key generated from torch UI
* ENABLE_VERSION_CHECK - This is used to enable or disable version compatibility check between Torch and SDK. Default Value is 'True'. To disable version check please set it to 'False'.


### Creating Airflow connection
If you want to avoid using environment variables then you can create a connection in Airflow UI as described below and provide the connection id of that connection in TorchInitializer.
Set the following in connection:
* Conn id: Create a unique ID for the connection
* Conn Type: HTTP
* Host - URL of the torch catalog
* Login - API access key generated from torch UI
* Password - API secret key generated from torch UI
* Extra - {"ENABLE_VERSION_CHECK": "{{value}}"}. This value will be used to enable or disable version compatibility check between Torch and SDK. Default Value is 'True'. To disable version check please set it to 'False'.

First of all, install below mentioned 2 pypi package to expose ETL in torch.
```bash
pip install acceldata-sdk
```

Read more about acceldata-sdk from [here](https://pypi.org/project/acceldata-sdk/)

```bash
pip install acceldata-airflow-sdk
```


Read more about acceldata-airflow-sdk from [here](https://pypi.org/project/acceldata-airflow-sdk/)

## Create TorchClient

While creating a TorchClient connection to torch by default version compatibility checks between torch and sdk is disabled. If we want we can Enable that check by passing `do_version_check` as `True`


```python
from acceldata-sdk.torch_client import TorchClient
torchClient = TorchClient(
    url="https://torch.acceldata.local:5443",
    access_key="OY2VVIN2N6LJ",
    secret_key="da6bDBimQfXSMsyyhlPVJJfk7Zc2gs",
    do_version_check=False
)
```


## Create DAG
In airflow DAG code, import torch dag instead of airflow dag. All the parameters will be the same as standard apache airflow dag. But there will be 2 additional parameters `override_success_callback`, `override_failure_callback`. 

Params:

`override_success_callback`: A Boolean parameter to allow the user to override the success callback provided by the SDK. The success callback end the pipeline run when DAG ends successfully. Default value is False. It should be set to True if we do not want the pipeline run to be ended at the end of the successful run of the DAG.

`override_failure_callback`: A Boolean parameter to allow the user to override the failure callback provided by the SDK. The failure callback ends the pipeline run with error when DAG ends in failure. Default value is False. It should be set to True if we do not want the pipeline run to be ended at the end of the unsuccessful run of the DAG.

These can be useful if few steps of the pipeline are being executed outside of Airflow DAG.
```python
from acceldata_airflow_sdk.dag import DAG
dag = DAG(
   dag_id='pipeline_demo_final',
   schedule_interval='@daily',
   default_args=default_args,
   start_date=datetime(2020, 2, 2),
   catchup=False,
   on_failure_callback= failure_callback,
   on_success_callback= success_callback,
   override_success_callback=False,
   override_failure_callback=False,
)
```




## Create Job and Span using decorator
This was added in version 0.0.36 <br />
To create a job and span in the pipeline, the user needs to decorate the python function with a job decorator as shown in the below example.


Object of `Node` should have either asset_uid (
{data source}.{asset path from its root}) or job_uid (Uid of next Job) as parameters.

Params:

`span_uid`: A String parameter to specify the UID of span to be created. Default value is None. If `span_uid` is not provided a span corresponding to the job will be created with value of job_uid.

`job_uid`: A String parameter to specify the job UID of the pipeline. Default value is None. If `job_uid` is not provided, uid is constructed using the task id and function name.

`inputs`: An Array parameter of Node type objects being used by job as input. Default value is empty array.

`outputs`: An Array parameter of Node type objects being returned by job as output. Default value is empty array.

`metadata`: Parameter of type JobMetadata specifying the metadata of the job. Default value is None.

`xcom_to_event_mapper_ids`: A list Parameter having list of xcom keys used to send xcom variables in span event. Default value is empty list.

`bounded_by_span`: A boolean parameter deciding whether to create a span along with the Job. Default value is True. If its is set to True to create span make sure, it has `**context` parameter inside the function argument. That gives access to the context of the task. Using the context, various span events can be sent inside the function. Use span_context = context['span_context_parent'] to get you the span context.

| NOTE: Passing context is mandatory to the function being decorated as our decorators use context to share information through xcom. |
|-------------------------------------------------------------------------------------------------------------------------------------|

| NOTE: The job_id for a task should be unique in a pipeline. |
|-------------------------------------------------------------|

If there are multiple tasks being created from a job decorated function then do not pass job_uid as that will end up using same job_uid for multiple tasks. In this scenario if we do not pass job_uid the autogenerated job_uid will be unique.

```python
from acceldata_airflow_sdk.decorators.job import job
from acceldata_sdk.models.job import JobMetadata, Node
@job(job_uid='monthly.order.aggregate.job',
   inputs=[Node(asset_uid='POSTGRES_LOCAL_DS.pipeline.pipeline.customer_orders')],
   outputs=[Node(job_uid='Job2_uid')],
   metadata=JobMetadata(name = 'Vaishvik_brahmbhatt', team = 'backend', code_location ='https://github.com/acme/reporting/report.scala'),
   span_uid='customer.orders.datagen.span',
   xcom_to_event_mapper_ids = ['run_id', 'event_id'],
   bounded_by_span=True
   )
def monthly_order_aggregate(**context):
    pass
```



## Create Span Using Decorator
To create a span for a python function, the user can decorate a python function with a span decorator that contains span uid as parameters. To decorate function with span make sure, it has `**context` parameter inside the function argument. That gives access to the context of the task. Using the context, various span events can be sent inside the function.  To get the parent span context, use the key name `span_context_parent` in xcom pull of the task instance. It’s value will be span context instance which can  be used to create child spans and send custom events (As shown in below example.)

Params:

`span_uid`: A String parameter to specify the UID of span to be created. Default value is None. If `span_uid` is not provided, uid is constructed using the task id and function name.

`xcom_to_event_mapper_ids`: A Parameter having list of xcom keys used to send xcom variables in span event. Default value is empty list.

| NOTE: Passing context is mandatory to the function being decorated as our decorators use context to share information through xcom. |
|-------------------------------------------------------------------------------------------------------------------------------------|
```python
from acceldata_airflow_sdk.decorators.span import span
from acceldata_sdk.events.generic_event import GenericEvent
@span(span_uid='customer.orders.datagen.span',
      associated_job_uids = ['monthly.order.aggregate.transfer'],  xcom_to_event_mapper_ids = ['run_id', 'event_id'] )
def data_gen(**context):
   datagen_span_context = context['span_context_parent']
   # Send event for current span
   datagen_span_context.send_event(
      GenericEvent(
         context_data={
            'client_time': str(datetime.now()), 
            'detail': 'Generating data'
         }, 
         event_uid="order.customer.join.result"
      )
   )
   customer_datagen_span = datagen_span_context.create_child_span(
       uid="customer.data.gen", 
      context_data= {'client_time': str(datetime.now()) }
   )
   # Send event for child span
   customer_datagen_span.send_event(
      GenericEvent(
         context_data={
            'client_time': str(datetime.now()), 
            'row_count': len(rows)
         }, 
         event_uid="order.customer.join.result"
      )
   )
   customer_datagen_span.end(
       context_data={'client_time': str(datetime.now()), 'customers_count': len(customer_ids) }
   )

```


## Custom Operators
Acceldata airflow sdk contains 4 custom operators.
##### TorchInitializer Operator:
The user needs to add a task with a given operator at the root of your dag. This operator will create a new pipeline. Additionally, this will create new pipeline run and root span for that dag run of the airflow dag.

Params:

`create_pipeline`: A Boolean parameter deciding whether to create a pipeline(if not exists) and pipeline run. Default Value is True. This can be useful if pipeline/pipeline run has been created outside of Airflow DAG.

`span_name`: A string parameter specifying name of the Root Span. Default value is None. If not provided we will use the pipeline_uid.span as span name.

`meta`: A parameter specifying the metadata for pipeline (PipelineMetadata). Default value is None. If not provided PipelineMetadata(owner='sdk/pipeline-user', team='TORCH', codeLocation='...') is set as meta. 

`pipeline_uid`: A string parameter specifying the UID of the pipeline. It is a mandatory parameter.

`pipeline_name`: A string parameter specifying the Name of the pipeline. Default value is None. If not provided pipeline_uid will be used as name.

`continuation_id`: A string parameter that uniquely identifies a pipeline run. This parameter can accept jinja templates as well. Default value is None. This parameter is useful when we want to have a pipeline run span over multiple DAG's. To use it we need to provide a continuation id while creating pipeline in first DAG with create_pipeline=True and then provide the same continuation id in the second DAG where we want to continue the same pipeline run with create_pipeline=False.

`connection_id`: A string parameter that uniquely identifies a connection storing Torch credentials. Default value is None. This parameter is useful when we want to use Torch credentials from Airflow connection instead of environment variables. To get details about creating a connection refer 'Creating Airflow connection' section above. 


```python
from acceldata_airflow_sdk.operators.torch_initialiser_operator import TorchInitializer
from acceldata_sdk.models.pipeline import PipelineMetadata

# example of jinja templates being used in continuation_id
# jinja template to pull value from config json
# continuation_id=f"{{{{ dag_run.conf['continuation_id']  }}}}"
# jinja template to pull value from xcom
# continuation_id=f"{{{{ task_instance.xcom_pull(key='continuation_id') }}}}"

torch_initializer_task = TorchInitializer(
   task_id='torch_pipeline_initializer',
   pipeline_uid='customer.orders.monthly.agg.demo',
   pipeline_name='CUSTOMERS ORDERS MONTHLY AGG',
   continuation_id='heterogeneous_test',
   create_pipeline=True,
   span_name='customer.orders.monthly.agg.demo.span',
   meta=PipelineMetadata(owner='test', team='testing', codeLocation='...'),
   dag=dag
)

```

##### SpanOperator Operator :
SpanOperator Operator will execute any std operator being passed as `operator` parameter and send span start and end event it. Just wrap the std operator with a span operator.
Make sure that the wrapped operator is not added in the DAG. If the operator is wrapped with a span operator, the span operator will take care of that operator task inside its execution. 

Params:

`span_uid`: A string parameter specifying the UID of span to be created. If `job_uid` is not provided, uid is constructed using the task id and operator name.

`xcom_to_event_mapper_ids`: A list parameter having list of xcom keys used to send xcom variables in span event. Default value is empty list.

`operator` : A parameter specifying the Standard airflow operator. It is a mandatory parameter.

Other parameters will be the same as the airflow standard base operator.

| WARNING: Do not specify the `dag` parameter in std airflow operator being passed as an argument to SpanOperator as the execution of operator task is taken care of by SpanOperator.   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
 
```python
from acceldata_airflow_sdk.operators.span_operator import SpanOperator

get_order_agg_for_q4 = PostgresOperator(
   task_id="get_monthly_order_aggregate_last_quarter",
   postgres_conn_id='example_db',
   sql="select * from information_schema.attributess",
)

get_order_agg_for_q4 = SpanOperator(
   task_id="get_monthly_order_aggregate_last_quarter",
   span_uid='monthly.order.agg.q4.span',
   operator=get_order_agg_for_q4,
   associated_job_uids = ['monthly.order.aggregate.transfer'],  
   xcom_to_event_mapper_ids = ['run_id', 'event_id'] ,
   dag=dag
)
```

##### JobOperator Operator :
JobOperator Operator will execute any std operator being passed as `operator` parameter and create a job and send span start and end event. Just wrap the std operator with a Job operator.
Make sure that the wrapped operator is not added in the DAG. If the operator is wrapped with a Job operator, the Job operator will take care of that operator task inside its execution. 

Object of `Node` should have either asset_uid (
{data source}.{asset path from its root}) or job_uid (Uid of next Job) as parameters.

Params:

`span_uid`: A string parameter to specify the UID of span to be created. Default value is None. If `span_uid` is not provided a span corresponding to the job will be created with value of job_uid.

`job_uid`: A string parameter to specify the job UID of the pipeline. Default value is None. If `job_uid` is not provided, uid is constructed using the task id and operator name.

`inputs`: An array parameter of Node type objects being used by job as input. Default value is empty array.

`outputs`: An array parameter of Node type objects being returned by job as output. Default value is empty array.

`metadata`: A parameter of type JobMetadata specifying the metadata of the job. Default value is None.

`xcom_to_event_mapper_ids`: A list parameter having list of xcom keys used to send xcom variables in span event. Default value is empty list.

`bounded_by_span`: A boolean parameter deciding whether to create a span along with the Job. Default value is True. If its is set to True to create span make sure, it has `**context` parameter inside the function argument. That gives access to the context of the task. Using the context, various span events can be sent inside the function. Use span_context = context['span_context_parent'] to get you the span context.

`operator` : A Parameter specifying the Standard airflow operator. It is a mandatory parameter.

Other parameters will be the same as the airflow standard base operator.
Make sure, inside a Node the type of the object which will have asset_uid (
{data source}.{asset path from its root}) or job_uid (Uid of next Job) as parameters.

| WARNING: Do not specify the `dag` parameter in std airflow operator being passed as an argument to JobOperator as the execution of operator task is taken care of by JobOperator.  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
 
```python
from acceldata_airflow_sdk.operators.job_operator import JobOperator
from acceldata_sdk.models.job import Node, JobMetadata
get_order_agg_for_q4 = PostgresOperator(
   task_id="get_monthly_order_aggregate_last_quarter",
   postgres_conn_id='example_db',
   sql="select * from information_schema.attributess",
)

get_order_agg_for_q4 = JobOperator(
   task_id="get_monthly_order_aggregate_last_quarter",
   job_uid='customer.order.join.job',
   inputs=[Node(asset_uid='POSTGRES_LOCAL_DS.pipeline.pipeline.orders'), Node(asset_uid='POSTGRES_LOCAL_DS.pipeline.pipeline.customers')] ,
   outputs=[Node(job_uid='next_job_uid')],
   metadata=JobMetadata('name', 'team', 'code_location'),
   span_uid='monthly.order.agg.q4.span',
   operator=get_order_agg_for_q4,
   xcom_to_event_mapper_ids = ['run_id', 'event_id'] ,
   bounded_by_span = True,
   dag=dag
)
```


##### ExecutePolicyOperator Operator : 
`ExecutePolicyOperator` is used to execute a policy by passing `policytype` and `policy_id`.

Params:

`sync`: A boolean parameter used to decide if the policy should be executed synchronously or asynchronously. It is a mandatory parameter. If it is set to  `True` it will return only after the execution ends. If it is set to `False` it will return immediately after starting the execution.

`policy_type`: A PolicyType parameter used to specify the policy type. It is a mandatory parameter. It is a enum which will take values from constants as PolicyType.DATA_QUALITY or PolicyType.RECONCILIATION.

`policy_id`: A string parameter used to specify the policy id to be executed. It is a mandatory parameter. 

`incremental`: A boolean parameter used to specify if the policy execution should be incremental or full. Default value is False.

`failure_strategy`: An enum parameter used to decide the behaviour in case of failure. Default value is DoNotFail.

* `failure_strategy` takes enum of type `FailureStrategy` which can have 3 values DoNotFail, FailOnError and FailOnWarning.

* DoNotFail will never throw. In case of failure it will log the error.
* FailOnError will Throw exception only if it's an error. In case of warning it return without any errors.
* FailOnWarning will Throw exception on warning as well as error.

```python
from acceldata_airflow_sdk.operators.execute_policy_operator import ExecutePolicyOperator
from acceldata_sdk.constants import FailureStrategy, PolicyType
operator_task = ExecutePolicyOperator(
    task_id='torch_pipeline_operator_test',
    policy_type=PolicyType.DATA_QUALITY,
    policy_id=46,
    sync=True,
    failure_strategy=FailureStrategy.DoNotFail,
    dag=dag
)
```

`ExecutePolicyOperator` stores the execution id of the policy executed in xcom using the key {`policy_type.name`}_{`policy_id`}_execution_id. Replace the policy_type and policy_id based on the policy.

Hence, to query the result in another task you need to pull the execution id from xcom using the same key {`policy_type`}_{`policy_id`}_execution_id 

`get_polcy_execution_result` can be used to query the result using the execution id pulled from xcom.
In this example the policy_type is const.PolicyType.DATA_QUALITY.name and the policy_id is 46.

Params:

`policy_type`:  A PolicyType parameter used to specify the policy type. It is a mandatory parameter. It is a enum which can take values from constants as PolicyType.DATA_QUALITY or PolicyType.RECONCILIATION.

`execution_id`: A string parameter specifying the execution id for which we want to query the results. It is a mandatory parameter. 

`failure_strategy`: An Enum parameter used to decide the behaviour in case of failure. Default value is DoNotFail.

* `failure_strategy` takes enum of type `FailureStrategy` which can have 3 values DoNotFail, FailOnError and FailOnWarning.
    
* DoNotFail will never throw. In case of failure it will log the error.
* FailOnError will Throw exception only if it's an error. In case of warning it return without any errors.
* FailOnWarning will Throw exception on warning as well as error.


```python
from acceldata_sdk.torch_client import TorchClient
from acceldata_airflow_sdk.initialiser import torch_credentials
from acceldata_sdk.constants import FailureStrategy, PolicyType, RuleExecutionStatus

def ruleoperator_result(**context):
    xcom_key = f'{PolicyType.DATA_QUALITY.name}_46_execution_id'
    task_instance = context['ti']
    # pull the execution id from xcom
    execution_id = task_instance.xcom_pull(key=xcom_key)
    if execution_id is not None:
        torch_client = TorchClient(**torch_credentials)
        result = torch_client.get_polcy_execution_result(policy_type=PolicyType.DATA_QUALITY, execution_id=execution_id,
                                                        failure_strategy=FailureStrategy.DoNotFail)
    if result.execution.resultStatus == RuleExecutionStatus.ERRORED:
        print(result.execution.executionError)
```


`get_policy_status` can be used to  query the current status of execution.

Params:

`policy_type`:  A PolicyType parameter used to specify the policy type. It is a mandatory parameter. It is an enum which can take values from constants as PolicyType.DATA_QUALITY or PolicyType.RECONCILIATION.

`execution_id`: A string parameter specifying the execution id which we want to query the status. It is a mandatory parameter.

You need to pull the execution id from xcom using the same key {`policy_type.name`}_{`policy_id`}_execution_id which was pushed by `ExecutePolicyOperator`. Replace the policy_type and policy_id based on the policy. In this example the policy_type is PolicyType.DATA_QUALITY.name and the policy_id is 46.




```python
from acceldata_sdk.torch_client import TorchClient
from acceldata_airflow_sdk.initialiser import torch_credentials
import acceldata_sdk.constants as const
def ruleoperator_status(**context):
    xcom_key = f'{const.PolicyType.DATA_QUALITY.name}_46_execution_id'
    task_instance = context['ti']
    # pull the execution id from xcom
    execution_id = task_instance.xcom_pull(key=xcom_key)
    if execution_id is not None:
        torch_client = TorchClient(**torch_credentials)
        result = torch_client.get_policy_status(policy_type=const.PolicyType.DATA_QUALITY, execution_id=execution_id)
        if result==const.RuleExecutionStatus.ERRORED:
            print("Policy execution encountered an error.")

```