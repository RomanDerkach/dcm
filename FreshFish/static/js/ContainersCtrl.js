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

        $scope.StartContainer = function(container_id){
            $http({
                method: 'POST',
                url: '/api/start_container',
                data: {'container_id': container_id}
                }).then(function successCallback(response){
                    $scope.LoadContainers();
                }, function errorCallback(response) {

                });
        };

        $scope.StopContainer = function(container_id){
            $http({
                method: 'POST',
                url: '/api/stop_container',
                data: {'container_id': container_id}
                }).then(function successCallback(response){
                    $scope.LoadContainers();
                }, function errorCallback(response) {

                });
        };

        $scope.RestartContainer = function(container_id){
            $http({
                method: 'POST',
                url: '/api/restart_container',
                data: {'container_id': container_id}
                }).then(function successCallback(response){
                    $scope.LoadContainers();
                }, function errorCallback(response) {

                });
        };

        $scope.DeleteContainer = function(container_id){
            $http({
                method: 'DELETE',
                url: '/api/del_container',
                data: {'container_id': container_id}
                }).then(function successCallback(response){
                    $scope.LoadContainers();
                }, function errorCallback(response) {

                });
        };



    }
]);
