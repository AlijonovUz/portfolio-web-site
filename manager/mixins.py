import time

from django.core.cache import cache
from django.contrib import messages
from django.shortcuts import redirect


class ThrottlingMixin:
    throttle_timeout = 60

    def dispatch(self, request, *args, **kwargs):
        if self.is_throttled(request):
            return self.handle_throttling(request)
        return super().dispatch(request, *args, **kwargs)

    def is_throttled(self, request):
        if request.user.is_authenticated:
            key = f"comment_throttle_user_{request.user.id}"
        else:
            key = f"comment_throttle_ip_{request.META.get('REMOTE_ADDR')}"

        last_comment_time = cache.get(key)
        if last_comment_time and time.time() - last_comment_time < self.throttle_timeout:
            return True

        cache.set(key, time.time(), timeout=self.throttle_timeout)
        return False

    def handle_throttling(self, request):
        messages.error(request, "Juda tez-tez izoh yuboryapsiz. Iltimos, biroz kuting.")
        return redirect(request.META.get('HTTP_REFERER', '/'))

