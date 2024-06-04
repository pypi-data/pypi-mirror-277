/*
 *
 * django-codenerix
 *
 * Codenerix GNU
 *
 * Project URL : http://www.codenerix.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

angular
    .module('codenerixFilters', [])

    .filter(
        'codenerix',
        function() {
            return function(input, kind) {
                if ((kind == null) || (kind == undefined)) {
                    // No kind defined
                    if ((input === null) || (input === undefined) ||
                        (input === '')) {
                        return '-';
                    } else if (input == 'True' || input === true) {
                        return '<i class="autotrue text-success glyphicon glyphicon-ok"></i>';
                    } else if (input == 'False' || input === false) {
                        return '<i class="autofalse text-danger glyphicon glyphicon-remove"></i>';
                    } else {
                        return input;
                    }
                } else if ((kind == 'none') || (kind == '')) {
                    return input;
                } else if (kind == 'bool') {
                    if ((input === null) || (input === undefined) ||
                        (input === '') || (!input)) {
                        return '<i class="autofalse text-danger glyphicon glyphicon-remove"></i>';
                    } else {
                        return '<i class="autotrue text-success glyphicon glyphicon-ok"></i>';
                    }
                } else if (kind == 'skype') {
                    return '<a ng-click=\'$event.stopPropagation();\' href=\'tel:' +
                           input + '\'>' + input + '</a>';
                } else if (kind.substring(0, 2) == 'qr') {
                    // qr:size
                    if ((input === null) || (input === undefined) ||
                        (input === '')) {
                        return `<button
                                    ng-click="$event.stopPropagation();"
                                    ng-disabled="true"
                                    class="btn btn-danger btn-xs">
                                    <i class="fa fa-qrcode" aria-hidden="true"></i>
                                </button>`;
                    } else {
                        var kind = kind.substring(3);
                        if (kind.length) {
                            bigsize = kind;
                        } else {
                            var bigsize = 200;
                        }
                        return `<div
                                ng-click="$event.stopPropagation();"
                                ng-init="qrsize=null; bigsize=` +
                               bigsize + `">
                                <button
                                    class="btn btn-info btn-xs"
                                    ng-show="qrsize==null"
                                    ng-click="$event.stopPropagation();qrsize=bigsize">
                                        <i class="fa fa-qrcode" aria-hidden="true"></i>
                                </button>
                                <button
                                    class="btn btn-xs"
                                    ng-hide="qrsize==null"
                                    ng-click="$event.stopPropagation();qrsize=null">
                                    <qr
                                        type-number="0"
                                        correction-level="'M'"
                                        ng-model="qrsize"
                                        size="qrsize"
                                        input-mode="'8bit'"
                                        text="'` +
                               input + `'"
                                        image="true">
                                    </qr>
                                </button>
                            </div>`;
                    }

                } else if (kind.substring(0, 4) == 'link') {
                    if ((input == null) || (input == undefined) ||
                        (input == '')) {
                        return '-';
                    } else {
                        var kind = kind.substring(5);
                        var kindsp = kind.split(':');
                        var blank = '';
                        var icon = '';
                        var text = input;
                        for (var i = 0; i < kindsp.length; i++) {
                            if (kindsp[i] == 'blank') {
                                blank = ' target="_blank"';
                            } else if (kindsp[i] == 'icon') {
                                icon =
                                    '<i class=\'glyphicon glyphicon-download-alt\'></i>';
                            } else if (kindsp[i] == 'onlyicon') {
                                icon =
                                    '<i class=\'glyphicon glyphicon-download-alt\'></i>';
                                text = '';
                            }
                        }
                        return `<a ng-click='$event.stopPropagation();' ` +
                               blank + ` href='` + input + `'>` + icon + ' ' +
                               text + `</a>`;
                    }
                } else if (kind.substring(0, 15) == 'copytoclipboard') {
                    if ((input == null) || (input == undefined) ||
                        (input == '')) {
                        return '-';
                    } else {
                        var kind = kind.substring(16);
                        if (kind.length) {
                            kingsp = kind.split(':');
                            if (kingsp.length == 1) {
                                var title = 'Info';
                                var body = kingsp[0];
                            } else {
                                var title = kingsp[0];
                                var body = kingsp[1];
                            }
                            var ngclick = `ng-click="modalinfo('` + title +
                                          `','` + body + `', 2000);"`;
                        } else {
                            var ngclick = '';
                        }

                        return `<a href="#" ng-click="$event.stopPropagation();">
                                <div
                                    ` +
                               ngclick + `
                                    codenerix-copy-to-clipboard="` +
                               input + `">
                                    <i
                                        class='fa fa-clipboard'
                                        aria-hidden='true'></i> ` +
                               input + `
                            </div>
                           </a>`;
                    }
                } else if (kind.substring(0, 5) == 'image') {
                    if ((input == null) || (input == undefined) ||
                        (input == '')) {
                        return '-';
                    } else {
                        if (kind == 'image') {
                            return '<img src=\'' + input + '\'  />';
                        } else {
                            var style = kind.substring(6);
                            return '<img src="' + input + '" style="' + style +
                                   '"  />';
                        }
                    }
                } else if (kind.substring(0, 5) == 'round') {
                    if ((input == null) || (input == undefined) ||
                        (input == '')) {
                        return '-';
                    } else if (kind == 'round') {
                        return '' + Math.round(input);
                    } else {
                        var decimals = kind.substring(6);
                        return Math.round(input * Math.pow(10, decimals)) /
                               Math.pow(10, decimals);
                    }

                } else if (kind.substring(0, 5) == 'money') {
                    if ((input == null) || (input == undefined) ||
                        (input == '')) {
                        return '-';
                    } else {
                        var kind = kind.substring(6);
                        if (kind == 'euro') {
                            return '' + Math.round(input * 100) / 100 + '€';
                        } else if (kind == 'dollar') {
                            return '$' + Math.round(input * 100) / 100;
                        } else if (kind == 'pound') {
                            return '£' + Math.round(input * 100) / 100;
                        } else if (kind == 'yuan') {
                            return '¥' + Math.round(input * 100) / 100;
                        } else if (kind == 'bitcoin') {
                            return '' + Math.round(input * 100) / 100 +
                                   '<span class=\'fa fa-btc\'></span>';
                        } else {
                            return input + '?';
                        }
                    }
                } else {
                    console.error(
                        'AngularJS filter \'codenerix\' got a wrong kind named \'' +
                        kind + '\'');
                    return input;
                }
            };
        })

    .filter(
        'nicenull',
        function() {
            return function(input) {
                return input ? input : '---';
            };
        })

    .filter(
        'choice_match',
        function() {
            return function(input, source) {
                var answer = input + '*';
                angular.forEach(source, function(e) {
                    if (e[0] == input) {
                        answer = e[1];
                        return;
                    }
                });
                return answer;
            };
        })
    .filter(
        'split',
        function() {
            return function(input, splitChar, splitIndex) {
                // do some bounds checking here to ensure it has that index
                return input.split(splitChar)[splitIndex];
            }
        })

    .filter(
        'highlightRow',
        function() {
            return function(text, search) {
                if (!search) {
                    return text;
                }
                return text.replace(
                    new RegExp(search, 'gi'), '<mark>$&</mark>');
            }
        })

    .filter(
        'highlightSelect',
        function() {
            function escapeRegexp(queryToEscape) {
                return queryToEscape.replace(/([.?*+^$[\]\\(){}|-])/g, '\\$1');
            };

            return function(matchItem, query) {
                return query && matchItem ?
                           matchItem.replace(
                               new RegExp(escapeRegexp(query), 'gi'),
                               '<span class="ui-select-highlight">$&</span>') :
                           matchItem;
            };
        })

    .filter(
        'weekday',
        function() {
            return function(input) {
                var result = '---';

                if (input == 1)
                    result = 'Monday'
                    else if (input == 2)
                    result = 'Tuesday'
                    else if (input == 3)
                    result = 'Wednesday'
                    else if (input == 4)
                    result = 'Thursday'
                    else if (input == 5)
                    result = 'Friday'
                    else if (input == 6)
                    result = 'Saturday'
                    else if (input == 7)
                    result = 'Sunday'

                    return result;
            };
        })

    .filter(
        'abs',
        function() {
            return function(val) {
                return Math.abs(val);
            }
        })

    .filter(
        'length',
        function() {
            return function(dict) {
                var count = 0;
                angular.forEach(dict, function(value, key) {
                    count++;
                });
                return count;
            }
        })

    .filter(
        'base64_encode',
        function() {
            return function(val) {
                return btoa(val);
            }
        })

    .filter(
        'base64_decode',
        function() {
            return function(val) {
                return atob(val);
            }
        })

    .filter(
        'htmlToPlaintext',
        function() {
            return function(text) {
                return angular.element(text).text();
                // return  text ? String(text).replace(/<[^>]+>/gm, '') : '';
            };
        })

    .filter(
        'strReplace',
        function() {
            return function(input, from, to) {
                input = input || '';
                from = from || '';
                to = to || '';
                return input.replace(new RegExp(from, 'g'), to);
            };
        })

    .filter(
        'default',
        function() {
            return function(input, defaultValue) {
                if (angular.isUndefined(input) || input === null ||
                    input === '') {
                    return defaultValue;
                } else {
                    return input;
                }
            }
        })

    .filter(
        'cut',
        function() {
            return function(value, wordwise, max, tail) {
                if (!value) return '';

                max = parseInt(max, 10);
                if (!max) return value;
                if (value.length <= max) return value;

                value = value.substr(0, max);
                if (wordwise) {
                    var lastspace = value.lastIndexOf(' ');
                    if (lastspace !== -1) {
                        // Also remove . and , so its gives a cleaner result.
                        if (value.charAt(lastspace - 1) === '.' ||
                            value.charAt(lastspace - 1) === ',') {
                            lastspace = lastspace - 1;
                        }
                        value = value.substr(0, lastspace);
                    }
                }

                return value + (tail || ' ...');
            };
        })

    .filter('round', function() {
        return function(input, decimals) {
            return Math.round(input * Math.pow(10, decimals)) /
                   Math.pow(10, decimals);
        };
    });
