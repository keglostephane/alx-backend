import { createQueue } from 'kue';

const queue = createQueue();

const jobData = {
  phoneNumber: '12345678',
  message: 'test job',
};

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`${job.id}`);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
