app.controller('ImagesCtrl', ['$scope', '$http',
    function($scope, $http){

        $scope.LoadImages = function(){
            $http({
                method: 'GET',
                url: 'api/all_images'
            }).then(function successCallback(response) {
                $scope.images = response.data
                console.log($scope.images)
            }, function errorCallback(response) {

            });
        };
        $scope.LoadImages();
    }
]);
