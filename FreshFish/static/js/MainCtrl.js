app.controller('MainCtrl', ['$scope', '$location', '$log',
      function($scope, $location, $log){
        $scope.selectedIndex = 0;
        $scope.$watch('selectedIndex', function(current, old) {
            switch (current) {
                case 0:
                    $location.url("/images");
                    break;
                case 1:
                    $location.url("/containers");
                    break;
            }
        });
      }
]);
