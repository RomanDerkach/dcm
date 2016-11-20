app.controller('ImagesCtrl', ['$scope', '$http',
    function($scope, $http){

        $scope.LoadImages = function(){
            $http({
                method: 'GET',
                url: '/api/all_images'
            }).then(function successCallback(response) {
                $scope.images = response.data
                console.log($scope.images)
            }, function errorCallback(response) {

            });
        };
        $scope.LoadImages();

        $scope.RunContainer = function(image_name_tag){
            $http({
                method: 'POST',
                url: '/api/run_container',
                data: {'image_name_tag': image_name_tag}
                }).then(function successCallback(response){
            });
        };

        $scope.DeleteImage = function(image_name_tag){
            $http({
                method: 'DELETE',
                url: '/api/del_image',
                data: {'image_name_tag': image_name_tag}
                }).then(function successCallback(response){
                    $scope.LoadImages();
                }, function errorCallback(response) {

                });
        };

    }
]);
