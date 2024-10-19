/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "mopu8mzkegy8heg",
    "created": "2024-10-14 11:47:28.065Z",
    "updated": "2024-10-14 11:47:28.065Z",
    "name": "Response",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "r1jurtzw",
        "name": "texte",
        "type": "text",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      }
    ],
    "indexes": [],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("mopu8mzkegy8heg");

  return dao.deleteCollection(collection);
})
