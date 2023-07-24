This is a python cli app which is used as a pomodoro timer.

We will be :
- using click module to interact with the CLI
- making the app in a simplified manner; it will be:
  - having a --time tag in minutes to specify the total time(default: 30mins with 25min of pomodoro and 5 mins of break)
  - having a --cycle tag to specify how many times it should go on(default = 1)
  - having a --break tag in minutes to specify the duration of breaks(default: 5mins)
  - having a progress bar to measure the time
- deploying the app in a nix package