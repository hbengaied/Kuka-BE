const request = require("request");

const MongoClient = require("mongodb").MongoClient;
url = "mongodb://127.0.0.1:27017/"; // c'est le lien vers la base de donnée

class make_all_request{
    constructor(){

        make_request_for_aztro();
        // setInterval(make_request_for_aztro,1);

        function make_request_for_aztro(){

            let all_signs = ['aries','taurus' , 'gemini' , 'cancer' , 'leo' , 'virgo' ,'libra' , 'scorpio' , 'sagittarius' , 'capricorn' , 'aquarius' , 'pisces'];

            let all_days = ['today' , 'tomorrow' , 'yesterday'];

            let signs_taked_randommly = all_signs[Math.floor(Math.random() * (0,all_signs.length))]

            let day_taked_randommly = all_days[Math.floor(Math.random() * (0,all_days.length))]


            var options = {
                url: 'https://aztro.sameerkumar.website/?sign='+ signs_taked_randommly +'&day='+ day_taked_randommly,
                method: 'POST'
            };
            
            request(options, (error,response,body) => {
                // Je commence à mettre cette donnée dans la base de donnée
                let db_connection = MongoClient.connect(url);
                db_connection.then(dbMongo => {
            
                const database_topic = dbMongo.db("DB_Bur_Etude");
            
                const collection_topic = database_topic.collection("Collection_Bur_Etude");
            
                const body_parsed = JSON.parse(body); // Je parse le JSON pour mettre ce que je veux dans mongo

                /*
                '{"date_range": "Mar 21 - Apr 20", "current_date": "February 9, 2023", "description": "Be cool. Sure, it would be nice to jump up and do whatever's in your head -- and then change directions as quickly as a new idea pops into being -- but that's not a good way to get things done. Have a little patience.", "compatibility": "Taurus", "mood": "Patient", "color": "Silver", "lucky_number": "78", "lucky_time": "2am"}\n'
                */
                // Il faut que je UpDate l'object ayant le sujet = signe_astronomique

                // filter est le filtre qui va indiquer l'objet ayant le même sujet
                const filter = { Sujet: "signe_astronomique" };
                // this option instructs the method to create a document if no documents match the filter
                const options = { upsert: false };
                // create a document that sets the plot of the movie
                const updateDoc = {
                $set: {
                    Sign: signs_taked_randommly,
                    Description: body_parsed.description,
                    Mood: body_parsed.mood,
                    lucky_number: body_parsed.lucky_number
                },
                };

                collection_topic.updateOne(filter, updateDoc, options);

                });
            });
        }
    }
}

new make_all_request();