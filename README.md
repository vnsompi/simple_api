Explication de la fonction update ot delete 

📌 Définition
@api_view(['PUT', 'DELETE'])
def update_or_delete_item(request, pk):


@api_view(['PUT', 'DELETE']) : indique que cette vue accepte uniquement les requêtes HTTP PUT (mise à jour) et DELETE (suppression).

pk : c’est l’identifiant (primary key) de l’objet Item qu’on veut modifier ou supprimer.

📌 Étape 1 : Récupérer l’objet
try:
    item = Item.objects.get(pk=pk)
except Item.DoesNotExist:
    return Response(status=404)


On essaie de récupérer l’item avec l’identifiant donné.

Si l’objet n’existe pas, on retourne une erreur 404 (Not Found).

📌 Étape 2 : Mise à jour (PUT)
if request.method == 'PUT':
    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


On initialise un serializer en lui passant :

item → l’objet existant à mettre à jour.

request.data → les nouvelles données envoyées par le client (JSON ou autre).

serializer.is_valid() → vérifie si les données sont correctes.

Si c’est valide : serializer.save() met à jour l’objet en base de données.

On retourne les données mises à jour.

Sinon, on retourne les erreurs avec un status 400 (Bad Request).

📌 Étape 3 : Suppression (DELETE)
elif request.method == 'DELETE':
    item.delete()
    return Response(status=204)


Si la méthode est DELETE, on supprime simplement l’objet.

On retourne un status 204 (No Content), ce qui signifie que l’opération s’est bien passée mais qu’il n’y a rien à renvoyer.

📌 Résumé rapide

PUT /items/<id>/ → met à jour l’item avec les nouvelles données.

DELETE /items/<id>/ → supprime l’item.

Retourne les bons codes HTTP :

200 → mise à jour réussie.

400 → données invalides.

404 → item inexistant.

204 → suppression réussie.

Veux-tu que je t’écrive aussi la version avec les classes génériques DRF (UpdateAPIView, DestroyAPIView) qui fait la même chose mais en beaucoup plus court ?

