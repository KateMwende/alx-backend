import redis, { createClient, print} from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
  console.log(`Received ${message} on ${channel}`);

  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
}
});