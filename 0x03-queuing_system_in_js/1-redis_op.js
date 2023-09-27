import redis, { createClient } from 'redis';

// Create a Redis client

const client = createClient();

// When the connection works
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// when the connection fails
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});


function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
};

function displaySchoolValue(schoolName) {
  client.get(schoolName, (_err, reply) => {
    console.log(reply);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
