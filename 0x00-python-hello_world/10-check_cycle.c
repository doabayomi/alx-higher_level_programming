#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a singly linked list
 * @list: The singly linked list to check
 *
 * Return: 1 if there is a cycle, 0 if there are no cycles
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *tmp_node;

	current = list;
	while (current != NULL)
	{
		tmp_node = current;
		while (tmp_node != NULL)
		{
			if (tmp_node->next == current)
				return (1);
			tmp_node = tmp_node->next;
		}
		current = current->next;
	}
	return (0);
}
