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

        In Prefix/Polish notation, operand and operator are distributed as <operator><operand><operand> and in Postfix/Inveverse Polish notation, operand and operator are distributed as <operand><operand><operator>
    

        | **Infix** | **Prefix** | **Postfix** |
        | :---- | :---  | :---  |
        | 2 + 3 | + 2 3 | 2 3 + |
        | p - q | - p q | p q - |
        | a + b * c | + a * b c | a b c * + |

Stack is implemented using:
* **Arrays:** 
    * Languages like **Python** allows developers to work easily because list objects already have operations like append(), pop() and arr[-1] which basically perform push(), pop() and top() operations 

    ```python
    arr = []
    arr.append(2) #push(8)
    arr.append(5)
    arr.append(10)
    arr #[2, 5, 10]
    arr[-1] #top() -> 8
    arr.pop() 
    arr #[2, 5]
    ```  

    * In C, all operations need to be implemented.

    ```C
        #include<stdio.h>
        #define MAX_SIZE 101
        int A[MAX_SIZE]; // integer array to store the stack 
        int top = -1;  // variable to mark top of stack in array

        // Push operation to insert an element on top of stack. 
        void Push(int x) {
        if(top == MAX_SIZE -1) { // overflow case. 
                printf("Error: stack overflow\n");
                return;
            }
            A[++top] = x;
        }
        // Pop operation to remove an element from top of stack.
        void Pop() {
            if(top == -1) { // If stack is empty, pop should throw error. 
                printf("Error: No element to pop\n");
                return;
            }
            top--;
        }
        // Top operation to return element at top of stack. 
        int Top() {
            return A[top];
        }
        // This function will return 1 (true) if stack is empty, 0 (false) otherwise
        int IsEmpty(){
            if(top == -1) return 1;
            return 0;
        }
        // This function is just to test the implementation of stack. 
        // This will print all the elements in the stack at any stage. 
        void Print() {
            int i;
            printf("Stack: ");
            for(i = 0;i<=top;i++)
                printf("%d ",A[i]);
            printf("\n");
        }
        int main() {	
            Push(2);
            Push(5);
            Push(10);
            Pop();
            Push(12);
        }
    ```    
