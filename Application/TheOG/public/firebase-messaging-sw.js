// Import and configure the Firebase SDK
// These scripts are made available when the app is served or deployed on Firebase Hosting
// If you do not serve/host your project using Firebase Hosting see https://firebase.google.com/docs/web/setup
/**
 * importScripts('/__/firebase/9.2.0/firebase-app-compat.js');
importScripts('/__/firebase/9.2.0/firebase-messaging-compat.js');
importScripts('/__/firebase/init.js');

const messaging = firebase.messaging(); */


/**
 * Here is is the code snippet to initialize Firebase Messaging in the Service
 * Worker when your app is not hosted on Firebase Hosting.
 * */
 // Give the service worker access to Firebase Messaging.
 // Note that you can only use Firebase Messaging here. Other Firebase libraries
 // are not available in the service worker.

 importScripts('https://www.gstatic.com/firebasejs/9.2.0/firebase-app-compat.js');
 importScripts('https://www.gstatic.com/firebasejs/9.2.0/firebase-messaging-compat.js');

 // Initialize the Firebase app in the service worker by passing in
 // your app's Firebase config object.
 // https://firebase.google.com/docs/web/setup#config-object

 firebase.initializeApp({
    apiKey: "AIzaSyB_Agu_4g-qA9drarU7jiChC3NAyUKcj30",
    authDomain: "the-og-27e6f.firebaseapp.com",
    databaseURL: "https://the-og-27e6f-default-rtdb.firebaseio.com",
    projectId: "the-og-27e6f",
    storageBucket: "the-og-27e6f.appspot.com",
    messagingSenderId: "729039730771",
    appId: "1:729039730771:web:8e406b1191c9ddbf1f2ea6",
    measurementId: "G-STFG704HHW",
 });
 
 // Retrieve an instance of Firebase Messaging so that it can handle background
 // messages.
 const messaging = firebase.messaging();




messaging.onBackgroundMessage(function(payload) {
    console.log('[firebase-messaging-sw.js] Received background message ', payload);
    // Customize notification here
    const notificationTitle = 'Background Message Title';
    const notificationOptions = {
      body: 'Background Message body.',
      icon: '/firebase-logo.png'
    };
  
    self.registration.showNotification(notificationTitle,
      notificationOptions);
  });