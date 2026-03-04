# Stack
Is a linear data structure in which the elements are inserted or removed from the same end, referred as the **top**. This DS is governed by the Last In, First Out **LIFO** principle,  which dictates that the last element introduced is the first one to be removed.

The following operations can be performed:
* **Push (O(1)):** An element is inserted at the top of the stack.
* **Pop (O(1)):** The element currently at the top is removed.
* **Top (O(1)):** The value of the element located at the top is returned without its removal.
* **IsEmpty (O(1)):** A boolean value is returned to indicate whether the stack is empty.

<video src="https://github.com/user-attachments/assets/a17987c8-43ac-4410-97c0-a586ee53ca01" controls autoplay muted width="400px">
  Tu navegador no admite el elemento de video.
</video>

Stack can be utilized for several applications:
* **Function calls or recursion (The Call Stack):**
    * When a function is called within another, the return address and local variables are stored at the top of the stack.
    * Once the execution of a function is completed, a pop operation is performed to release that allocated memory and control is returned exactly to the point where the previous execution was interrupted. 
* **Implement Undo/Redo operations:**
    * Two stacks are required, one for **Undo** and another for **Redo**.
    * Every new action is represented by a push operation into the Undo Stack. When the ```Ctrl + Z``` command is triggered, the most recent state is popped from the Undo Stack and pushed into the Redo Stack, allowing the state to be recovered if necessary.
* **Compiler verification of Balanced Parentheses:**
    * A sequence is considered balanced if a corresponding closing symbol is provided for every opening symbol.
    * The expression is traversed by the compiler; whenever an opening symbol is encountered, it is pushed onto the stack. When a closing symbol is found, it is compared with the element at the top of the stack to ensure a valid match.
* **Evaluate prefix and postfix notation:**
    * Unlike infix notation which requires dos parentheses and precedence rules for it to be unambiguous, prefix and postfix notation dictate the order by default.
    ...Prefix Notation or Polish notation is 


# Queue