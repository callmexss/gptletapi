from celery import shared_task
from .models import SubmitTask, GPTEntry
from .apify_helper import build_gpts_link_dict, fetch_urls, extract_items, convert_item_to_entry_obj


@shared_task
def check_and_process_submit_tasks():
    print("call task")
    tasks = SubmitTask.objects.filter(finished=False)
    urls = [build_gpts_link_dict(task.link_url) for task in tasks]
    try:
        print("Get gpts info.")
        run = fetch_urls(urls)
        items = extract_items(run)

        for task, item in zip(tasks, items):
            try:
                print(f"save task: {task.link_url}")
                entry_data = convert_item_to_entry_obj(item)
                gpt, created = GPTEntry.objects.get_or_create(
                    unique_link_url=entry_data['link_url'],
                )
                if created:
                    gpt.name = entry_data['title']
                    gpt.description = entry_data['description']
                    gpt.image_url = entry_data['logoUrl']
                    gpt.link_url = entry_data['link_url']
                    gpt.author = entry_data['author']

                task.finished = True
                task.save()

            except Exception as e:
                error_message = f"Error processing task: {str(e)}"
                task.notes = error_message
                task.save()
    except Exception as err:
        print(err)
