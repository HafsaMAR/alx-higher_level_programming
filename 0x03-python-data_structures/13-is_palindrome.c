#include "lists.h"

int is_palindrome(listint_t **head)
{
    int n = 0, i = 0, j = 0;
    listint_t *half_2_node, *half_1_node, *current = *head;
    half_1_node = *head;
    half_2_node = *head;

    if (!head)
    {
        return (1);
    }
    while (current)
    {
        current = current->next;
        n++;
    }
    while (j < n / 2)
    {
        half_2_node = half_2_node->next;
        j++;
    }
    j = 0;
    while (n / 2 + j > n && half_2_node)
    {
        half_2_node = half_2_node->next;
        while (i < n / 2 - j)
        {
            half_1_node = half_1_node->next;
        }
        if (half_2_node->n != half_1_node->n)
        {
            return (0);
        }
        j++;
    }
    return (1);
}