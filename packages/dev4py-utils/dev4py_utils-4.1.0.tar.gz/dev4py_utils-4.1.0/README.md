# Dev4py-utils

A set of Python regularly used classes/functions

[![ci](https://github.com/dev4py/dev4py-utils/actions/workflows/ci.yml/badge.svg?event=push&branch=main)](https://github.com/dev4py/dev4py-utils/actions/workflows/ci.yml) \
[![Last release](https://github.com/dev4py/dev4py-utils/actions/workflows/on_release.yml/badge.svg)](https://github.com/dev4py/dev4py-utils/actions/workflows/on_release.yml) \
[![Weekly checks](https://github.com/dev4py/dev4py-utils/actions/workflows/weekly_checks.yml/badge.svg?branch=main)](https://github.com/dev4py/dev4py-utils/actions/workflows/weekly_checks.yml) \
[![Python >= 3.11](https://img.shields.io/badge/Python->=3.11-informational.svg?style=plastic&logo=python&logoColor=yellow)](https://www.python.org/) (See: [Older Python versions compatibility](#older-python-versions-compatibility)) \
[![Maintainer](https://img.shields.io/badge/maintainer-St4rG00se-informational?style=plastic&logo=superuser)](https://github.com/St4rG00se) \
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=plastic&logo=github) \
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-yellow.svg?style=plastic&logo=github)](https://opensource.org/licenses/Apache-2.0)

## Table of contents

- [Quickstart](#quickstart)
- [Project template](#project-template)
- [Project links](#project-links)
- [Older Python versions compatibility](#older-python-versions-compatibility)
- [Dev4py-utils modules](#dev4py-utils-modules)
  - [dev4py.utils.AsyncJOptional](#dev4pyutilsasyncjoptional)
  - [dev4py.utils.awaitables](#dev4pyutilsawaitables)
  - [dev4py.utils.collectors](#dev4pyutilscollectors)
  - [dev4py.utils.dicts](#dev4pyutilsdicts)
  - [dev4py.utils.iterables](#dev4pyutilsiterables)
  - [dev4py.utils.JOptional](#dev4pyutilsjoptional)
  - [dev4py.utils.lists](#dev4pyutilslists)
  - [dev4py.utils.objects](#dev4pyutilsobjects)
  - [dev4py.utils.pipeline](#dev4pyutilspipeline)
  - [dev4py.utils.retry](#dev4pyutilsretry)
  - [dev4py.utils.Stream](#dev4pyutilsstream)
  - [dev4py.utils.tuples](#dev4pyutilstuples)
  - [dev4py.utils.types](#dev4pyutilstypes)

## Quickstart

```shell
pip install dev4py-utils
```

## Project template

This project is based on [pymsdl_template](https://github.com/dev4py/pymsdl_template)

## Project links

- [Documentation](https://dev4py.github.io/dev4py-utils/)
- [PyPi project](https://pypi.org/project/dev4py-utils/)

## Older Python versions compatibility

- [Python >= 3.10.1](https://www.python.org/) -> [dev4py-utils 3.6.0](https://github.com/dev4py/dev4py-utils/tree/3.6.0)

## Dev4py-utils modules

### dev4py.utils.AsyncJOptional

[AsyncJOptional documentation](https://dev4py.github.io/dev4py-utils/dev4py/utils/async_joptional.html)

> ***Note:** [AsyncJOptional](src/main/python/dev4py/utils/async_joptional.py) class is designed in order to simplify
> JOptional with async mapper.*

> ***Note:** AsyncJOptional support T or Awaitable[T] values. That's why some checks are done when terminal operation is
> called with `await`.*

Examples:

```python
import asyncio
from dev4py.utils import AsyncJOptional

def sync_mapper(i: int) -> int:
  return i * 2

async def async_mapper(i: int) -> str:
  return f"The value is {i}"

async def async_sample() -> None:
  value: int = 1
  await AsyncJOptional.of_noneable(value) \
    .map(sync_mapper) \
    .map(async_mapper) \
    .if_present(print)  # The value is 2

asyncio.run(async_sample())
```

### dev4py.utils.awaitables

[Awaitables documentation](https://dev4py.github.io/dev4py-utils/dev4py/utils/awaitables.html)

> ***Note:** [awaitables](src/main/python/dev4py/utils/awaitables.py) module provides a set of utility functions to
> simplify Awaitable operations.*

Examples:

```python
import asyncio
from dev4py.utils import awaitables, JOptional

# is_awaitable sample
awaitables.is_awaitable(asyncio.sleep(2))  # True
awaitables.is_awaitable(print('Hello'))  # False


# to_sync_or_async_param_function sample
def mapper(s: str) -> str:
    return s + '_suffix'

async def async_mapper(s: str) -> str:
    await asyncio.sleep(1)
    return s + '_async_suffix'

async def async_test():
    # Note: mapper parameter is str and async_mapper returns an Awaitable[str] so we have to manage it
    # Note: !WARNING! Since 3.0.0 see AsyncJOptional / JOptional to_async_joptional method
    result: str = await JOptional.of("A value") \
      .map(async_mapper) \
      .map(awaitables.to_sync_or_async_param_function(mapper)) \
      .get()
    print(result)  # A value_async_suffix_suffix

asyncio.run(async_test())
````

### dev4py.utils.collectors

[Collectors documentation](https://dev4py.github.io/dev4py-utils/dev4py/utils/collectors.html)

> ***Note:** The [collectors](src/main/python/dev4py/utils/collectors.py) class is inspired by
> [java.util.stream.Collectors](https://docs.oracle.com/en/java/javase/17/docs/api//java.base/java/util/stream/Collectors.html)*

Examples:

```python
from dev4py.utils import Stream, collectors

Stream.of('a', 'b', 'c').collect(collectors.to_list())  # ['a', 'b', 'c']
```

### dev4py.utils.dicts

[Dicts documentation](https://dev4py.github.io/dev4py-utils/dev4py/utils/dicts.html)

> ***Note:** [dicts](src/main/python/dev4py/utils/dicts.py) module provides a set of utility functions to
> simplify dict operations.*

Examples:

```python
from dev4py.utils import dicts
from dev4py.utils.types import Supplier

# is_dict sample
dicts.is_dict("A str")  # False
dicts.is_dict({'key': 'A dict value'})  # True


# get_value sample
int_supplier: Supplier[int] = lambda: 3
dictionary: dict[str, int] = {'key_1': 1, 'key_2': 2}

dicts.get_value(dictionary, 'key_1')  # 1
dicts.get_value(dictionary, 'key_3')  # None
dicts.get_value(dictionary, 'key_3', int_supplier)  # 3


# get_value_from_path sample
str_supplier: Supplier[str] = lambda: "a3"
deep_dictionary: dict[str, dict[int, str]] = { \
  'a': {1: 'a1', 2: 'a2'}, \
  'b': {1: 'b1', 2: 'b2'} \
}

dicts.get_value_from_path(deep_dictionary, ["a", 1])  # 'a1'
dicts.get_value_from_path(deep_dictionary, ["c", 1])  # None
dicts.get_value_from_path(deep_dictionary, ["a", 3])  # None
dicts.get_value_from_path(deep_dictionary, ["a", 3], str_supplier)  # 'a3'
````

### dev4py.utils.iterables

[Iterables documentation](https://dev4py.github.io/dev4py-utils/dev4py/utils/iterables.html)

> ***Note:** The [iterables](src/main/python/dev4py/utils/iterables.py) module provides a set of utility functions to simplify
> iterables operations.*

Example:

```python
from typing import Iterator

from dev4py.utils import iterables

values: range = range(0, 10)
chunks: Iterator[list[int]] = iterables.get_chunks(values, 3)
[chunk for chunk in chunks]  # [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
```

### dev4py.utils.JOptional

[JOptional documentation](https://dev4py.github.io/dev4py-utils/dev4py/utils/joptional.html)

> ***Note:** [JOptional](src/main/python/dev4py/utils/joptional.py) class is inspired by
> [java.util.Optional](https://docs.oracle.com/en/java/javase/17/docs/api//java.base/java/util/Optional.html)
> class with some adds (like `peek` method).*

Examples:

```python
from dev4py.utils import JOptional

value: int = 1
JOptional.of_noneable(value) \
  .map(lambda v: f"The value is {v}") \
  .if_present(print)  # The value is 1
```

### dev4py.utils.lists

[Lists documentation](https://dev4py.github.io/dev4py-utils/dev4py/utils/lists.html)

> ***Note:** [lists](src/main/python/dev4py/utils/lists.py) module provides a set of utility functions to simplify lists
> operations.*

Examples:

```python
from dev4py.utils import lists

# empty sample
lst: list[int] = lists.empty_list()  # []

# append sample
lst: list[int] = [1, 2, 3, 4]
app_lst: list[int] = lists.append(lst, 5)  # [1, 2, 3, 4, 5]
# - Note: lst == app_lst

# extend sample
lst: list[int] = [1, 2, 3, 4]
lst2: list[int] = [5, 6, 7, 8]
ext_lst: list[int] = lists.extend(lst, lst2)  # [1, 2, 3, 4, 5, 6, 7, 8]
# - Note: lst == ext_lst
```

### dev4py.utils.objects

[Objects documentation](https://dev4py.github.io/dev4py-utils/dev4py/utils/objects.html)

> ***Note:** The [objects](src/main/python/dev4py/utils/objects.py) module is inspired by
> [java.util.Objects](https://docs.oracle.com/en/java/javase/17/docs/api//java.base/java/util/Objects.html)
> class.*

Examples:

```python
from dev4py.utils import objects

# non_none sample
value = None
objects.non_none(value)  # False

# require_non_none sample
value = "A value"
objects.require_non_none(value)  # 'A value'

# to_string sample
value = None
default_value: str = "A default value"
objects.to_string(value, default_value)  # 'A default value'
```

### dev4py.utils.pipeline

[Pipeline documentation](https://dev4py.github.io/dev4py-utils/dev4py/utils/pipeline.html)

> ***Note:** The [pipeline](src/main/python/dev4py/utils/pipeline) package provides a set of Pipeline class describing
> different kind of pipelines.*

Examples:

```python
from dev4py.utils.pipeline import SimplePipeline, StepPipeline, StepResult

# SimplePipeline sample
pipeline: SimplePipeline[int, str] = SimplePipeline.of(lambda i: i * i) \
    .add_handler(str) \
    .add_handler(lambda s: f"Result: {s} | Type: {type(s)}")

pipeline.execute(10)  # "Result: 100 | Type: <class 'str'>"


# StepPipeline sample
# Note: StepPipeline can be stopped at each step by setting `go_next` value to False
pipeline: StepPipeline[int, str] = StepPipeline.of(lambda i: StepResult(i * i)) \
    .add_handler(lambda i: StepResult(value=str(i), go_next=i < 150)) \
    .add_handler(lambda s: StepResult(f"Result: {s} | Type: {type(s)}"))

pipeline.execute(10)  # StepResult(value="Result: 100 | Type: <class 'str'>", go_next=True)
# - Note: When the pipeline is fully completed, `go_next` is True
pipeline.execute(15)  # StepResult(value='225', go_next=False)
# - Note: Even if the pipeline is not fully completed, the last StepResult is returned with `go_next=False`
```

### dev4py.utils.retry

[Retry documentation](https://dev4py.github.io/dev4py-utils/dev4py/utils/retry.html)

> ***Note:** The [retry](src/main/python/dev4py/utils/retry.py) module provides provides function to create retryable
> callable from simple sync or async callables using exponential backoff*
>
> *Usage idea: network requests (HTTP, AMQP, MQTT, etc.) with retry on error*

Examples:

```python
import asyncio
from time import time
from typing import Awaitable

from dev4py.utils.retry import RetryConfiguration, to_retryable, to_async_retryable, retryable, async_retryable
from dev4py.utils.types import BiFunction

# RetryConfiguration:
# Note: exponential backoff used formula is 'delay * (exponent^retry_number)'
#
#   => Example: For the following RetryConfiguration, waiting times in case of error are:
#       * first try:                    0 sec (always 0 for the first try)
#       * second try (/first retry):    1 sec ('0.5 * (2^1)')
#       * third try (/second retry):    2 sec ('0.5 * (2^2)')
#       * max_tries=3 => no fourth try (/third retry)
retry_config: RetryConfiguration = RetryConfiguration(
    delay=0.5,  # the exponential backoff delay in second (default: 0.1)
    exponent=2,  # the exponential backoff exponent to determine delay between each try (default: 2)
    max_tries=3  # max try number (first try included) (default: 3, i.e.: first try and 2 retry)
)


# to_retryable sample:
# -> SUCCESSFUL CALL SAMPLE
def callable_sample(j: int, start_time: float) -> int:
    print("callable_sample - call time: '%.2f'" % (time() - start_time))
    return j ** 2

retryable_sample: BiFunction[int, float, int] = to_retryable(sync_callable=callable_sample, retry_config=retry_config)
# Note: Since 3.5.0 you can also use `retryable(sync_callable=callable_sample, retry_config=retry_config)`

result: int = retryable_sample(3, time())  # result = 9
# outputs:
#  callable_sample - call time: '0.00'


# -> IN ERROR CALL SAMPLE
def in_error_callable_sample(j: int, start_time: float) -> int:
    print("in_error_callable_sample - call time: '%.2f'" % (time() - start_time))
    raise ValueError(j)

in_error_retryable_sample: BiFunction[int, float, int] = \
    to_retryable(sync_callable=in_error_callable_sample, retry_config=retry_config)
# Note: Since 3.5.0 you can also use `retryable(sync_callable=in_error_callable_sample, retry_config=retry_config)`
# Note: By default the last raised exception is raised if max_tries is reach. You can change this behavior by setting
#       the `on_failure` parameter
result: int = in_error_retryable_sample(3, time())
# outputs:
#  in_error_callable_sample - call time: '0.00'
#  in_error_callable_sample - call time: '1.00'
#  in_error_callable_sample - call time: '3.00'
#  ValueError: 3
#
# Note: By default the last raised exception is raised if max_tries is reached. You can change this behavior by setting
#       the `on_failure` parameter

# -> DECORATOR SAMPLE
@retryable(retry_config=retry_config)
def decorated_in_error_callable_sample(j: int, start_time: float) -> int:
    print("decorated_in_error_callable_sample - call time: '%.2f'" % (time() - start_time))
    raise ValueError(j)

result: int = decorated_in_error_callable_sample(3, time())
# outputs:
#  decorated_in_error_callable_sample - call time: '0.00'
#  decorated_in_error_callable_sample - call time: '1.00'
#  decorated_in_error_callable_sample - call time: '3.00'
#  ValueError: 3
#
# Note: By default the last raised exception is raised if max_tries is reached. You can change this behavior by setting
#       the `on_failure` parameter


# to_async_retryable sample:
# -> IN ERROR CALL ASYNC SAMPLE
async def in_error_async_callable_sample(j: int, start_time: float) -> int:
    print("in_error_async_callable_sample - call time: '%.2f'" % (time() - start_time))
    raise ValueError(j)

async def async_retryable_sample() -> None:
    in_error_async_retryable_sample: BiFunction[int, float, Awaitable[int]] = \
        to_async_retryable(async_callable=in_error_async_callable_sample, retry_config=retry_config)
    # Note: Since 3.5.0 you can also use 
    # `async_retryable(async_callable=in_error_async_callable_sample, retry_config=retry_config)`
    result: int = await in_error_async_retryable_sample(2, time())

asyncio.run(async_retryable_sample())
# outputs:
#  in_error_async_callable_sample - call time: '0.00'
#  in_error_async_callable_sample - call time: '1.00'
#  in_error_async_callable_sample - call time: '3.00'
#  ValueError: 2
#
# Note: By default the last raised exception is raised if max_tries is reached. You can change this behavior by setting
#       the `on_failure` parameter

# -> DECORATOR ASYNC SAMPLE
@async_retryable(retry_config=retry_config)
async def decorated_in_error_async_callable_sample(j: int, start_time: float) -> int:
    print("decorated_in_error_async_callable_sample - call time: '%.2f'" % (time() - start_time))
    raise ValueError(j)

async def async_decorated_retryable_sample() -> None:
    result: int = await decorated_in_error_async_callable_sample(2, time())

asyncio.run(async_decorated_retryable_sample())
# outputs:
#  in_error_async_callable_sample - call time: '0.00'
#  in_error_async_callable_sample - call time: '1.00'
#  in_error_async_callable_sample - call time: '3.00'
#  ValueError: 2
#
# Note: By default the last raised exception is raised if max_tries is reached. You can change this behavior by setting
#       the `on_failure` parameter
```

### dev4py.utils.Stream

[Stream documentation](https://dev4py.github.io/dev4py-utils/dev4py/utils/stream.html)

> ***Note:** [Stream](src/main/python/dev4py/utils/stream.py) class is inspired by
> [java.util.stream.Stream](https://docs.oracle.com/en/java/javase/17/docs/api//java.base/java/util/stream/Stream.html).*

Examples:

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from time import sleep

from dev4py.utils import Stream, ParallelConfiguration

# Sequential sample
Stream.of(1, 2, 3, 4) \
    .map(str) \
    .peek(lambda s: sleep(0.5)) \
    .map(lambda s: f"Mapped value: {s}") \
    .to_list()  # ['Mapped value: 1', 'Mapped value: 2', 'Mapped value: 3', 'Mapped value: 4']
# - Note: Execution time around 2 sec due to the sleep call


# Multithreading sample
with ThreadPoolExecutor(max_workers=2) as executor:
    Stream.of(1, 2, 3, 4) \
        .parallel(parallel_config=ParallelConfiguration(executor=executor, chunksize=2)) \
        .map(str) \
        .peek(lambda s: sleep(0.5)) \
        .map(lambda s: f"Mapped value: {s}") \
        .to_list()  # ['Mapped value: 3', 'Mapped value: 4', 'Mapped value: 1', 'Mapped value: 2']
# - Note: Execution time around 1 sec due to the given ParallelConfiguration
# - Note: Since this stream is (by default) unordered, results order is random


# Multiprocessing sample
# - Note: Due to use of Multiprocessing:
#       * lambdas cannot be used since they cannot be pickled
#       * This sample should be put in a python file in order to work
def _sleep(s: str) -> None:
    # eq lambda s: sleep(0.5)
    sleep(0.5)

def _mapper(s: str) -> str:
    # eq lambda s: f"Mapped value: {s}"
    return f"Mapped value: {s}"

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as executor:
        Stream.of(1, 2, 3, 4) \
            .parallel(parallel_config=ParallelConfiguration(executor=executor, chunksize=2)) \
            .map(str) \
            .peek(_sleep) \
            .map(_mapper) \
            .to_list()

# - Note: Execution time around 1 sec due to the given ParallelConfiguration
#         (Reminder: Use Multiprocessing for CPU-bound tasks. In this case Multithreading is more appropriate)
# - Note: Since this stream is (by default) unordered, results order is random
```

### dev4py.utils.tuples

[Tuples documentation](https://dev4py.github.io/dev4py-utils/dev4py/utils/tuples.html)

> ***Note:** [tuples](src/main/python/dev4py/utils/tuples.py) module provides a set of utility functions to simplify
> tuples operations.*

Examples:

```python
from dev4py.utils import tuples

# empty sample
tpl: tuple[int, ...] = tuples.empty_tuple()  # ()

# append sample
tpl: tuple[int, ...] = (1, 2, 3, 4)
app_tpl: tuple[int, ...] = tuples.append(tpl, 5)  # (1, 2, 3, 4, 5)

# extend sample
tpl: tuple[int, ...] = (1, 2, 3, 4)
tpl2: tuple[int, ...] = (5, 6, 7, 8)
ext_tpl: tuple[int, ...] = tuples.extend(tpl, tpl2)  # (1, 2, 3, 4, 5, 6, 7, 8)
```

### dev4py.utils.types

[Types documentation](https://dev4py.github.io/dev4py-utils/dev4py/utils/types.html)

> ***Note:** The [types](src/main/python/dev4py/utils/types.py) module is inspired by
> [java.util.function](https://docs.oracle.com/en/java/javase/17/docs/api//java.base/java/util/function/package-summary.html)
> package.*

Examples:

```python
from dev4py.utils.types import Function, Predicate, Consumer

# Function sample
int_to_str: Function[int, str] = lambda i: str(i)
str_result: str = int_to_str(1)  # '1'

# Predicate sample
str_predicate: Predicate[str] = lambda s: s == "A value"
pred_result: bool = str_predicate("Value to test")  # False

# Consumer sample
def sample(consumer: Consumer[str], value: str) -> None:
    consumer(value)

def my_consumer(arg: str) -> None:
    print(arg)

sample(my_consumer, "My value")  # My value
```
