#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, *fast_ptr = *head,
		  *temp_ptr = *head, *dup_ptr = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast_ptr = fast_ptr->next->next;
		if (!fast_ptr)
		{
			dup_ptr = slow_ptr->next;
			break;
		}
		if (!fast_ptr->next)
		{
			dup_ptr = slow_ptr->next->next;
			break;
		}
		slow_ptr = slow_ptr->next;
	}

	reverse_listint(&dup_ptr);

	while (dup_ptr && temp_ptr)
	{
		if (temp_ptr->n == dup_ptr->n)
		{
			dup_ptr = dup_ptr->next;
			temp_ptr = temp_ptr->next;
		}
		else
			return (0);
	}

	if (!dup_ptr)
		return (1);

	return (0);
}
/**
 * reverse_listint - reverses a listint_t linked list
 * @head: pointer to pointer to the head of the linked list
 *
 * Description: This function reverses a linked list.
 * Return: void
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev_ptr = NULL;
	listint_t *current_ptr = *head;
	listint_t *next_ptr = NULL;

	while (current_ptr)
	{
		next_ptr = current_ptr->next;
		current_ptr->next = prev_ptr;
		prev_ptr = current_ptr;
		current_ptr = next_ptr;
	}

	*head = prev_ptr;
}
