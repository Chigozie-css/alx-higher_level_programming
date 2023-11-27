#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	if (list == NULL)
		return (0);
	while (fast != NULL && fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
