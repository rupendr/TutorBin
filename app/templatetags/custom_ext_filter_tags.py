from django import template

register = template.Library()


@register.filter
def checkStatus(id, name):
    """
    This function filter whether logged in user invested against any Borrower or not.
    if invested will display against Uninvest else display Invest text.

    :param inv_id:
    :param br_id:
    :return:
    """
    check_extension = ''
    if len(name) > 0:
        check_extension = name.split('.')[1]
    return check_extension
