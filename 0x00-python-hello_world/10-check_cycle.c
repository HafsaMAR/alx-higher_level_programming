#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
    /*int *address = &list->n;
    */listint_t *node = list;

    while (node)
    {
        if (node->next == list)
        {
            return (1);
        }
        node = node->next;
    }
    return (0);
}