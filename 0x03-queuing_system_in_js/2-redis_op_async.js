import util from 'util';
import redis, { createClient } from 'redis';

// Create a Redis client

const client = createClient();

// When the connection works
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// when the connection fails
client.on('error', (err) => {
  console.log('Redis client not connected to the server: ${err.message}');
});

// set key with value
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
};

// promiisfy the redis get method
const getAsync = util.promisify(client.get).bind(client);

// display value of key
async function displaySchoolValue(schoolName) {
  const result = await getAsync(schoolName).catch((error, result) => {
    if (error) {
      console.log(error);
      throw error;
    }
  });
  console.log(result);
};

// call the function
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
