
## Installation

To install, download the Tasker.py file and import it into your project folder.
```python
  from Tasker import t
```
**note** : Ensure that your project file and Tasker.py are in the same folder.

## Usage
First, import the Tasker module:
```python
from Tasker import t
```
Now, you can use Tasker in your project.

### t.print
Here are some examples for your reference.
#### **Simple Print:**
```python
t.print(message='hi')
```
![Output](https://s6.uupload.ir/files/capture_mxu.png)

The number 2 is the line number. If you don't provide any code option, the D tag will be used in the output. The MainModule is the name of the function that ran your code.

#### **Print With code:**
```python
t.print(message='error',code=2)
```
![Output](https://s6.uupload.ir/files/capture_2exe.png)

Code 2 is for error outputs. Use this code when you encounter an error.

**note*: Code range is from 0 to 3.

#### **Print With optional function name:**
```python
t.print(message='test',function_name='My Function Name')
```
![Output](https://s6.uupload.ir/files/capture_qimg.png)

As you can see, the MainModule changes to **My Function Name**. It's as if your code ran inside a function named "My Function Name".

### t.config
Currently, there are two configuration options available.

#### **filename**
```python
t.config(filename=True)
t.print(message='test')
```
![Output](https://s6.uupload.ir/files/capture_m4s.png)

Now, the output includes the name of your Python file at the beginning.

#### **timer**
```python
t.config(timer=True)
t.print(message='test')
```
![Output](https://s6.uupload.ir/files/capture_5aq0.png)

With this configuration, you can see the time taken for your code to execute the t.print(s) command.
