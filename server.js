require('dns').setServers(['8.8.8.8']);
const {MongoClient} = require('mongodb');
const express = require('express');
const app = express();
const dotenv = require('dotenv');
dotenv.config();
app.use(express.urlencoded({ extended: true }));
const port = 3000;
const client = new MongoClient(process.env.MONGODB_URI);
const db = client.db('studentDB');
const students = db.collection('students');
async function connect(){
    await client.connect();
    console.log("Connected to Mongodb");

    app.get('/',async(req,res)=>{
       res.sendFile(__dirname + '/index.html');
    })

    app.post('/submit',async(req,res)=>{
        const name = req.body.name;
        const age = req.body.age;
        await students.insertOne(
            {
                name:name,
                age:age
            }
        );
        res.send("Inserted");
    })
}
connect();
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});