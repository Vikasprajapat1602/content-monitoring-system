from .models import ContentItem
from .mock_data import mock_content
from django.utils.dateparse import parse_datetime
from .models import Flag
from django.utils.timezone import now
from .models import Keyword, ContentItem



def load_content():
    for item in mock_content:

        obj, created = ContentItem.objects.get_or_create(
            title=item["title"],
            source=item["source"],
            defaults={
                "body": item["body"],
                "last_updated": parse_datetime(item["last_updated"])
            }
        )

        


def calculate_score(keyword, content):
    keyword_lower = keyword.name.lower()
    title = content.title.lower()
    body = content.body.lower()

    # exact match in title
    if keyword_lower in title.split():
        return 100

    # partial match in title
    elif keyword_lower in title:
        return 70

    # match in body only
    elif keyword_lower in body:
        return 40

    return 0


# test function
def run_matching():
    keywords = Keyword.objects.all()
    contents = ContentItem.objects.all()

    results = []

    for keyword in keywords:
        for content in contents:
            score = calculate_score(keyword, content)

            if score > 0:
                results.append({
                    "keyword": keyword.name,
                    "content": content.title,
                    "score": score
                })

    return results





def generate_flags():
    keywords = Keyword.objects.all()
    contents = ContentItem.objects.all()

    created_flags = []

    for keyword in keywords:
        for content in contents:

            score = calculate_score(keyword, content)

            if score > 0:

                existing_flag = Flag.objects.filter(
                    keyword=keyword,
                    content_item=content
                ).first()

                # case 01 -> no flag then create
                if not existing_flag:
                    flag = Flag.objects.create(
                        keyword=keyword,
                        content_item=content,
                        score=score
                    )
                    created_flags.append(flag.id)

                else:
                    # case 2: irrelevant
                    if existing_flag.status == "irrelevant":

                        # suppression check
                        if existing_flag.last_reviewed_at and content.last_updated <= existing_flag.last_reviewed_at:
                            continue  

                        else:
                            existing_flag.score = score
                            existing_flag.status = "pending"
                            existing_flag.save()

                            created_flags.append(existing_flag.id)

                    # already relevant/pending
                    else:
                        continue

    return created_flags


def run_scan():

    load_content()

    # Generate flags
    created_flags = generate_flags()

    return {
        "message": "Scan completed",
        "flags_created": len(created_flags)
    }