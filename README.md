
## Usage
First import the Tasker
```python
from Tasker import t
```
now you can use tasker in your project.

### t.print
here is the examples for you.
#### **Simple Print:**
```python
t.print(message='hi')
```
![Output](https://s6.uupload.ir/files/capture_mxu.png)

the number 2 is the line Number! if you dont give any code option, we use **D** TAG in output.
and the MainModule is the name that function Ran your code

#### **Print With code:**
```python
t.print(message='error',code=2)
```
![Output](https://s6.uupload.ir/files/capture_2exe.png)

The code 2 is for Error outputs, my main is use this code, when you think got an Error.

**note*: Code Range = 0 to 3

#### **Print With optional function name:**
```python
t.print(message='test',function_name='My Function Name')
```
![Output](https://s6.uupload.ir/files/capture_qimg.png)

as you think the MainModule change to the **My Function Name**! its like my code ran in some function with the name My Function Name.

### t.config
for now we have just 2 option for config

#### **filename**
```python
t.config(filename=True)
t.print(message='test')
```
![Output](https://s6.uupload.ir/files/capture_m4s.png)

now we have the our file python code name on the first of the outputs

#### **timer**
```python
t.config(timer=True)
t.print(message='test')
```
![Output](https://s6.uupload.ir/files/capture_5aq0.png)

now you can see how much time speend for your code to get the t.print command
