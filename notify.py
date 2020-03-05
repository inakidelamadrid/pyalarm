import os


def notify(text, **kwargs):
    title = kwargs.get("title", "Notification")

    os.system(
        """
              osascript -e 'display notification "{}" with title "{}"'
              """.format(
            text, title
        )
    )
