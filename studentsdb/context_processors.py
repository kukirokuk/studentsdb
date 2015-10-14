from .settings import PORTAL_URL

def students_proc(request):
	return {'PORTAL_URL': PORTAL_URL}

TEMPLATE_CONTEXT_PROCESSORS = \
	global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
	"django.core.context_processors.request",
	"studentsdb.context_processors.students_proc",
)
