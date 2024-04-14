// Promises

export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success === true) {
      const objPass = {
        status: 200,
        body: 'Success',
      };
      resolve(objPass);
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
}
