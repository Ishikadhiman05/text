#include <stdio.h>
#include <stdlib.h>
struct Node{
      int data;
      struct Node* next;
};
struct Node* createnode( int value){
    struct Node* newnode=(struct Node*)malloc(sizeof(struct Node));
    newnode->data = value;
    newnode->next = NULL;
    return  newnode;
}
void displayList(struct Node* head){
        struct Node* temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

int main() {
    struct Node* head = NULL;
    head = createnode(10);
    head->next = createnode(20);
    head->next->next = createnode(30);


    printf("Singly Linked List\n ");
    displayList(head);

    return 0;
}
