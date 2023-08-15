#include "lists.h"

int is_palindrome(listint_t **head)
{
    int n = 0, j = 0, list[200];
    listint_t *current = *head;

    if (*head == NULL || (*head)->next != NULL)
    {
        return (1);
    }
    while (current)
    {
        list[n] = current->n;
        current = current->next;
        n++;
    }
    while (j < n / 2)
    {
        if (list[j] != list[n - j - 1])
            return (0);
        j++;
    }

    return (1);
}