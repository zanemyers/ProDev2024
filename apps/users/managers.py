from django.db.models import QuerySet, Q


class ProfileQuerySet(QuerySet):
    def search_profiles(self, search_query: str):
        """
        Search profiles by name, short_intro, or skill name.
        """
        return (
            self.filter(
                Q(name__icontains=search_query)
                | Q(short_intro__icontains=search_query)
                | Q(skill__name__icontains=search_query)
            )
            .prefetch_related("skill_set")
            .distinct()
        )
