#!/usr/bin/node

const request = require('request');

const completedTasks = (err, res, body) => {
  if (err) console.log(err);
  const usersTodos = {};
  const todos = JSON.parse(body);
  for (let i = 0; i < todos.length; i++) {
    if (todos[i].completed === true) {
      const userId = todos[i].userId.toString();
      if (userId in usersTodos) usersTodos[userId]++;
      else usersTodos[userId] = 1;
    }
  }
  console.log(usersTodos);
};
request(process.argv[2], completedTasks);
