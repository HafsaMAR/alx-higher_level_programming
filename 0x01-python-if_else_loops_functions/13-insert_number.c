#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *current_node = *head;
    listint_t *new_node = malloc(sizeof(listint_t));

    if (new_node == NULL)
        return (NULL);
    new_node->n = number;
    if (*head == NULL || (*head)->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }
    while (current_node && current_node->next->n < number)
    {
        current_node = current_node->next;
    }
    new_node->next = current_node->next;
    current_node->next = new_node;
    return (new_node);
}