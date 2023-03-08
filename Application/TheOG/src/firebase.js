import {getFunctions, httpsCallable} from "firebase/functions";
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getMessaging, getToken, onMessage } from "firebase/messaging";
import { getDatabase, ref, onValue } from "firebase/database";

const firebaseConfig = {
    apiKey: "AIzaSyB_Agu_4g-qA9drarU7jiChC3NAyUKcj30",
    authDomain: "the-og-27e6f.firebaseapp.com",
    databaseURL: "https://the-og-27e6f-default-rtdb.firebaseio.com",
    projectId: "the-og-27e6f",
    storageBucket: "the-og-27e6f.appspot.com",
    messagingSenderId: "729039730771",
    appId: "1:729039730771:web:8e406b1191c9ddbf1f2ea6",
    measurementId: "G-STFG704HHW"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const messaging = getMessaging(app);
const database = getDatabase(app);

// Request permission for notifications
function requestPermission() {
  Notification.requestPermission().then((permission) => {
    if (permission === "granted") {
      console.log("Notification permission granted.");
      getToken(messaging, {
        vapidKey:
          "BLfNwRYQKXcFixJOZ1ycv9mtc4l_g4tShgS6Gqdr2bSnHVrp5oiUMxeVdH9QqCB5yc1qNcRxUGhDCqNCisrQeuI",
      }).then((currentToken) => {
        if (currentToken) {
          console.log("currentToken: ", currentToken);
        } else {
          console.log("Can't get token");
        }
      });
    } else {
      console.log("Do not have permission!");
    }
  });
}

requestPermission();

// Set up a listener for new values added to the database
onValue(ref(database, "test"), (snapshot) => {
  const data = snapshot.val();
  console.log("New notification added: ", data);

  // Send the notification
  // const sendNotification = firebase.functions().httpsCallable("sendNotification");
  const sendNotification = httpsCallable(getFunctions(), "sendNotification");
  // sendNotification({ message: data.message })
  //   .then((result) => {
  //     console.log(result);
  //   })
  //   .catch((error) => {
  //     console.error(error);
  //   });
    sendNotification({})
    console.log("test");
    
});