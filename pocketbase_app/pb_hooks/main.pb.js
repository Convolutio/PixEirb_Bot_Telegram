//n'importe qui qui fait get_random_response peut voir une réponse random (pas d'authentification)
routerAdd("GET", "/get_random_response", (c) => {
    //qand on fait un /get_random_response on va donner un au hasard dans la liste
    const result = arrayOf(new DynamicModel({        "texte":    "",    }))
    $app.dao().db()
    .newQuery("SELECT texte FROM Response ORDER BY random() LIMIT 1")
    .all(result)

    return c.json(200, result[0])
})