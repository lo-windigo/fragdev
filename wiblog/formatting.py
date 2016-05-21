from django.utils.safestring import mark_safe
import CommonMark


# Convert a markdown string into HTML5, and prevent Django from escaping it
def mdToHTML(value):

    return mark_safe(CommonMark.commonmark(value))


# Sort posts by year
def postSort(posts):

    orderedPosts = {}

    for post in posts:

        if post.date.year not in orderedPosts:
            orderedPosts[post.date.year] = []

        orderedPosts[post.date.year].append(post)

    return sorted(orderedPosts, reverse)


# Get a summary of a post
def summarize(fullBody):

    firstNewline = fullBody.find("\n")

    if firstNewline > 0:
        return fullBody[:firstNewline]

    return fullBody
