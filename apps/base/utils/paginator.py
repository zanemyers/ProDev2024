from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate_list_object(request, object_list: list, results_per_page: int = 6, get_short_range: bool = True):
    """
    This function takes a request, a list of objects, and the number of results per page and returns a paginated object
    list and a custom range. This function should be used in conjunction with the pagination.html template.
    """
    current_page = request.GET.get("page", 1)
    object_paginator = Paginator(object_list, results_per_page)

    try:
        object_list = object_paginator.page(current_page)
    except PageNotAnInteger:
        current_page = 1
        object_list = object_paginator.page(current_page)
    except EmptyPage:
        current_page = object_paginator.num_pages
        object_list = object_paginator.page(current_page)

    page_range = object_paginator.page_range
    if get_short_range is True:
        page_range = _get_custom_range(object_paginator, current_page)

    return object_list, page_range


def _get_custom_range(object_paginator, current_page):
    """Returns a shorter range of pages to display in the pagination.html template."""
    left_index = (int(current_page) - 4)
    if left_index < 1:
        left_index = 1

    right_index = (int(current_page) + 5)
    if right_index > object_paginator.num_pages:
        right_index = object_paginator.num_pages + 1

    return range(left_index, right_index)
