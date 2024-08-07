# Too Many Variables!
The esolang where all you can do is assign variables.

## Table of Contents
* [How To Run *Too Many Variables!*](#how-to-run-too-many-variables)
* [How *Too Many Variables!* Works](#how-too-many-variables-works)

## How To Run *Too Many Variables!*
This *Too Many Variables!* (TMV) interpreter runs via the command line. Type <code>py \_\_init\_\_.py <i>&lt;code&gt;</i></code> to run *\<code\>*.

>[!IMPORTANT]
>Since TMV code generally has many line breaks, you may need to surround the code in quotes for the program to work.

In addition, you can add on some flags:
* `-c` or `--check` lets you check that the code you typed in was correct. If you don't like the code, type `No` (case-insensitive) in the prompt.
* `-h` or `--help` gives you a list of all of the arguments and options.

More flags will probably be added soon.

## How *Too Many Variables!* Works
TMV is actually a pretty simple programming language. Each line follows the format  
<code><i>&lt;number&gt;</i>=<i>&lt;number&gt;&lt;op&gt;&lt;number&gt;</i></code>,  
where *\<number\>* is a series of characters from `0` to `9`, and *\<op\>* is one of `+-*/`.

You may notice that the definition of *\<number\>* allows for leading zeroes. This is not only intentional, but required for any literal numbers or control flow (both of which are extremely important to TMV).

Here's a list of formats for numbers and what they mean:

| Format                        | Regex                | Description                   |
|-------------------------------|----------------------|-------------------------------|
| Number with no leading zeroes | `[1-9]\d*`           | Variable                      |
| Number with 1 leading zero    | `0[1-9]\d*`          | Literal number                |
| `000`                         | `000`                | Literal number 0              |
| `0`                           | `0`                  | **Special:** Input/output[^1] |
| `00`                          | `00`                 | **Special:** Line number[^2]  |
| Anything else                 | `00([1-9]\d*\|0\d+)` | Invalid&mdash;throws an error |

Meanwhile, the *\<op\>* can be one of four things.
* `+` is integer addition.
* `-` is integer subtraction.
* `*` is integer multiplication.
* `/` is integer division, rounded towards -&infin;. If the divisor is 0, it also returns 0.

This is actually the entire language! Examples of TMV code are at [examples.md](/../examples.md).

[^1]: Assigning a number to the `0` variable prints the number as a character.
  Accessing the `0` variable gets one character of input and returns its Unicode codepoint.
[^2]: Assigning a number to the `00` variable changes the line number of the instruction pointer to the number. If the new line number is outside of the range of the program, it halts instantly.
  Accessing the `00` variable gets the line number of the instruction pointer.
