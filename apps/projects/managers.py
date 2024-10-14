from django.db.models import QuerySet, Q


class ProjectQuerySet(QuerySet):
    def search_projects(self, search_query: str):
        """
        Search projects by title or description.
        """
        return (
            self.filter(
                Q(title__icontains=search_query)
                | Q(description__icontains=search_query)
                | Q(owner__name__icontains=search_query)
                | Q(tags__name__icontains=search_query)
            )
            .select_related("owner")
            .prefetch_related("tags")
            .distinct()
        )
