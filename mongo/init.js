db = db.getSiblingDB("blog_db");

db.createCollection("posts", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["titre", "auteur", "vues"],
      properties: {
        titre: { bsonType: "string" },
        auteur: { bsonType: "string" },
        vues:   { bsonType: "int" }
      }
    }
  }
});

db.posts.insertMany([
  { titre: "Docker Basics",  auteur: "Hiba",  vues: 10 },
  { titre: "MongoDB Intro",  auteur: "Hiba",  vues: 20 },
  { titre: "DevOps",         auteur: "John",  vues: 30 },
  { titre: "Containers",     auteur: "Alice", vues: 15 },
  { titre: "CI/CD",          auteur: "Bob",   vues: 50 }
]);