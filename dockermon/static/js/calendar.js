/* // Your Client ID can be retrieved from your project in the Google
                        // Developer Console, https://console.developers.google.com
                        var CLIENT_ID = '71843179415-gc0ci5oqfuc1snr4uiga8n6gtjl1tole.apps.googleusercontent.com';
                  
                        // This quickstart only requires read-only scope, check
                        // https://developers.google.com/google-apps/calendar/auth if you want to
                        // request write scope.
                        var SCOPES = ['https://www.googleapis.com/auth/calendar.readonly'];
                  
                        /**
                         * Check if current user has authorized this application.
                         */
                        function checkAuth() {
                          gapi.auth.authorize(
                            {
                              'client_id': CLIENT_ID,
                              'scope': SCOPES,
                              'immediate': true
                            }, handleAuthResult);
                        }
                  
                        /**
                         * Handle response from authorization server.
                         *
                         * @param {Object} authResult Authorization result.
                         */
                        function handleAuthResult(authResult) {
                          var authorizeDiv = document.getElementById('authorize-div');
                          if (authResult && !authResult.error) {
                            // Hide auth UI, then load Calendar client library.
                            authorizeDiv.style.display = 'none';
                            loadCalendarApi();
                          } else {
                            // Show auth UI, allowing the user to initiate authorization by
                            // clicking authorize button.
                            authorizeDiv.style.display = 'inline';
                          }
                        }
                  
                        /**
                         * Initiate auth flow in response to user clicking authorize button.
                         *
                         * @param {Event} event Button click event.
                         */
                        function handleAuthClick(event) {
                          gapi.auth.authorize(
                            {client_id: CLIENT_ID, scope: SCOPES, immediate: false},
                            handleAuthResult);
                          return false;
                        }
                  
                        /**
                         * Load Google Calendar client library. List upcoming events
                         * once client library is loaded.
                         */
                        function loadCalendarApi() {
                          gapi.client.load('calendar', 'v3', listUpcomingEvents);
                        }
                  
                        /**
                         * Print the summary and start datetime/date of the next ten events in
                         * the authorized user's calendar. If no events are found an
                         * appropriate message is printed.
                         */
                        function listUpcomingEvents() {
                          var request = gapi.client.calendar.events.list({
                            'calendarId': 'primary',
                            'timeMin': (new Date()).toISOString(),
                            'showDeleted': false,
                            'singleEvents': true,
                            'maxResults': 10,
                            'orderBy': 'startTime'
                          });
                  
                          request.execute(function(resp) {
                            var events = resp.items;
                  
                            console.log(events);
                           // appendPre('Upcoming events:');
                  
                            if (events.length > 0) {
                              for (i = 0; i < events.length; i++) {
                                var event = events[i];
                                var when = event.start.dateTime;
                                if (!when) {
                                  when = event.start.date;
                                }
                                var extra1 = "";
                                var extra2 = "";
                                
                                /*var tdy = new Date();
                                tdy = tdy.toISOString();
                                tdy = tdy.split("T");
                                tdy = tdy[0];
                                evt = when.split("T");
                                evt = evt[0];
                              //  evt = "2015-04-28";
                                console.log(evt);
                                var extra1 = "";
                                var extra2 = "";
                                if(tdy.string == evt.string ){
                                    alert("DDDD");
                                    extra1 = '<span style="background-color: #FFFF00">';
                                    extra2 = '</span>';
                                }*/
                                appendPre(extra1 + event.summary + ' (' + when + ')'+ extra2 +   event.location);
                              }
                            } else {
                              appendPre('No upcoming events found.');
                            }
                  
                          });
                        }
                  
                        /**
                         * Append a pre element to the body containing the given message
                         * as its text node.
                         *
                         * @param {string} message Text to be placed in pre element.
                         */
                        function appendPre(message) {
                          var pre = document.getElementById('output');
                       //   $(pre).append("<img src='static/images/Calander-Google-32.png' />&nbsp<li>");
                      //    $(pre).append("&nbsp<li>");
                         
                          var textContent = document.createTextNode(message + '\n');
                          
                       /*   var elem = document.createElement("img");
                          elem.setAttribute("src", "static/images/Calander-Google-32.png");
                          pre.appendChild(elem);*/

                          var h = document.createElement("hr");     
                        //   $(h).prepend("<img src='static/images/Calander-Google-32.png' />&nbsp");
                          pre.appendChild(textContent);
                          pre.appendChild(h);
                          
                   
                         // pre.innerHTML = message + '\n';
                        }*/