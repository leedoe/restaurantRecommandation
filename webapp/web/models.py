from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


# cluster_informations
class clusterInformations(models.Model):
    id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.id


# UserInformation
class UserInfo(AbstractUser):
    age = models.IntegerField(null=True)
    cluster_id = models.ForeignKey(clusterInformations, null=True)

    def __str__(self):
        return str(self.id)


# Food Information
class FoodInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=24)

    def __str__(self):
        return str(self.id)

# Food Base Tag
class FoodBaseTag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=24, unique=True)

    def __str__(self):
        return self.name

# Food Tags
class FoodTags(models.Model):
    foodId = models.ForeignKey(FoodInfo, 
        null=False,
        on_delete=models.CASCADE)
    tagId = models.ForeignKey(FoodBaseTag, 
        null=False, 
        on_delete=models.CASCADE)

    def __str__(self):
        return str(self.FoodId) + ", " + str(self.TagId)

    class Meta:
        unique_together = (("foodId", "tagId"),)


# Food recommendation
class FoodRecommendations(models.Model):
    userID = models.ForeignKey(UserInfo,
        on_delete=models.CASCADE)
    foodID = models.ForeignKey(FoodInfo,
        on_delete=models.CASCADE,
        primary_key=True)
    recommendation = models.IntegerField()


    def __str__(self):
        return str(self.foodID)

    class Meta:
        unique_together = (("userID", "foodID"),)


# User Preference
class UserEvaluations(models.Model):
    userID = models.ForeignKey(UserInfo,
        on_delete=models.CASCADE)
    foodID = models.ForeignKey(FoodInfo,
        on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return str(self.userID) + " " + str(self.foodID) + " " +str(self.score)

    class Meta:
        unique_together = (("userID", "foodID"),)


# Restaurant
class RestaurantInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=24)
    location = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


# Restaurant Menus
class RestaurantMenus(models.Model):
    restaurantId = models.ForeignKey(RestaurantInfo,
        on_delete=models.CASCADE)
    foodId = models.ForeignKey(FoodInfo,
        on_delete=models.CASCADE)

    class Meta:
        unique_together = (("restaurantId", "foodId"),)

    def __str__(self):
        return self.restaurantId

    


# cluster_tag_scores
class clusterTagScores(models.Model):
    cluster_id = models.ForeignKey(
        clusterInformations,
        on_delete=models.CASCADE)
    tag_id = models.ForeignKey(
        FoodBaseTag,
        on_delete=models.CASCADE)
    mean = models.FloatField(
        null=True)
    number = models.FloatField(
        null=True)

    def __str__(self):
        return self.cluster_id

    class Meta:
        unique_together = (("cluster_id", "tag_id"),)


# cluster_positions
class clusterPositions(models.Model):
    cluster_id = models.ForeignKey(
            clusterInformations,
            primary_key=True)
    tag_id = models.ForeignKey(
        FoodBaseTag)
    pos = models.FloatField()

    def __str__(self):
        return self.cluster_id

    class Meta:
        unique_together = (("cluster_id", "tag_id"),)


# cluster_food_scores
class clusterFoodScores(models.Model):
    cluster_id = models.ForeignKey(
            clusterInformations)
    tag_id = models.ForeignKey(
        FoodBaseTag)
    predictable_score = models.FloatField()

    def __str__(self):
        return self.cluster_id

    class Meta:
        unique_together = (("cluster_id", "tag_id"),)