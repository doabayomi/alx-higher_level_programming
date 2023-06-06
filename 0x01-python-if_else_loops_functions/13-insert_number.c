#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * *insert_node - inserts a node in sorted linked list
 * @head: Head of the linked list
 * @number: The number to be inserted
 *
 * Return: Pointer to the newly created node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *tmp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}

	current = *head;
	while (current->next != NULL)
	{
		if (number > current->n)
		{
			tmp = current->next;
			if (number < tmp->n)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			current = current->next;
			continue;
		}
		else
		{
			new->next = current;
			return (new);
		}
	}
	new->next = NULL;
	current->next = new;
	return (new);
}
