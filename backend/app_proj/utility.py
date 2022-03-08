"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
UTILITY
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import django.db as DB


def ConvertFigureToJson(figure):
    import json
    from plotly.utils import PlotlyJSONEncoder

    redata = json.loads(json.dumps(figure.data, cls=PlotlyJSONEncoder))
    relayout = json.loads(json.dumps(figure.layout, cls=PlotlyJSONEncoder))
    fig_json=json.dumps({'data': redata,'layout': relayout})

    return fig_json

class BaseManager(DB.models.Manager):
    def getOrNone(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None

def GetTableCounts():
    from django.apps import apps

    customTables = []
    for name, app in apps.app_configs.items():
            
        if name in ['admin', 'auth', 'contenttypes', 'sessions']:
            continue

        modelLs = list(app.get_models())

        for m in modelLs:
            customTables.append({
                'Module': name,
                'Table': str(m).split('.')[-1].replace("'>", ""),
                'Count': m.objects.count(),
            })

    return customTables




def InsertBulk(dataLs, table):
    # modelLs = [LegoSet(**r) for r in dataLs]
    # LegoSet.objects.bulk_create(modelLs)
    modelLs = eval(f"[TB.{table}(**r) for r in dataLs]")
    exec(f"TB.{table}.objects.bulk_create(modelLs, ignore_conflicts=True)")


def InsertSingle(entryDx, table):
    try:
        # newModel = LegoSet(**entryDx)
        # newModel.save()
        eval(f"")
    except Exception as ex:
        print(ex)
        print(entryDx)
        print('')





