

import yamp
def generateConfigMaps(poly: dict, currentNamespace, currentReleaseName):
    configMaps = []
    for projectName, map1 in poly.items():
        for namespace, map2 in map1.items():

            if namespace == currentNamespace:
                for releaseName, map3 in map2.items():

                    if releaseName == currentReleaseName:
                        for configMapName, items in map3.items():
                            configMaps.append(generateConfigMap(configMapName, items))
    return configMaps

def generateConfigMap(configMapName, items):
    bindings = yamp.new_globals()
    bindings['$name'] = configMapName
    bindings['$items'] = items
    result = yamp.expand_file('chart/templates/config-map-template.yaml', bindings, expandafterload=True)
    return result



