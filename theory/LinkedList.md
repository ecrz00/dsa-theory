# Linked List
A **Linked List** is a linear data strcutrure in which elements are not allocated in a contiguous block of memory. Instead, each element is defines as an object or structure referred to as **Node**.
A **Node** is composed of two primary attributes:
* **Value:** The data is stored or referenced within the node; this can be an integer, string, or any other data type.
* **Next:** A reference or pointer to the memory address of the subsequent node.

```python
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
```

```c
struct node{
    int value;
    struct node* next_node;
};
```
    
Two fundamental pointers are utilized to manage a Linked List:

* **Head:** This is a pointer that refers to the first element of the list. If the head pointer is lost or overwritten, the entire list becomes inaccessible from memory, resulting in a memory leak.
* **Tail:** This is identified as the final node in the sequence. To signify the end of the list, its Next attribute is set to ```NULL``` (in C) or ```None``` (in Python).

```mermaid
graph LR
    %% Referencia al inicio
    H((HEAD)) --> Node1

    %% Nodo 1
    subgraph Node1 [0xA200B]
        d1[7] --- p1["Next <br> 0xB7F14"]
    end
    
    %% Nodo 2
    subgraph Node2 [0xB7F14]
        d2[2] --- p2["Next <br> 0xF2230"]
    end

    %% Nodo 3
    subgraph Node3 [0xF2230]
        d3[1] --- p3["Next <br> NULL"]
    end

    %% Conexiones
    p1 --> Node2
    p2 --> Node3
    p3 --> NULL[(NULL)]

    %% Estilos: Lila traslúcido oscuro
    style Node1 fill:#2d2d3a80,stroke:#8B008B,color:#aaa
    style Node2 fill:#2d2d3a80,stroke:#8B008B,color:#aaa
    style Node3 fill:#2d2d3a80,stroke:#8B008B,color:#aaa
    
    style d1 fill:#1a1a1a,stroke:#ccc,color:#fff
    style d2 fill:#1a1a1a,stroke:#ccc,color:#fff
    style d3 fill:#1a1a1a,stroke:#ccc,color:#fff
    
    style p1 fill:#483D8B80,stroke:none,color:#fff
    style p2 fill:#483D8B80,stroke:none,color:#fff
    style p3 fill:#483D8B80,stroke:none,color:#fff
    
    style H fill:#2d2d3a,stroke:#8B008B,color:#fff
    style NULL fill:#1a1a1a,stroke:#ccc,color:#fff
```
