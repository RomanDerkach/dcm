app.controller('ContainersCtrl', ['$scope', '$http',
    function($scope, $http){

        $scope.LoadContainers = function(){
            $http({
                method: 'GET',
                url: '/api/all_containers'
            }).then(function successCallback(response) {
                $scope.containers = response.data
                console.log($scope.containers)
            }, function errorCallback(response) {

            });
        };
        $scope.LoadContainers();

    }
]);
