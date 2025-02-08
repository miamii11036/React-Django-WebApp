# 使用Django的預設User模型，管理與使用者認證相關的功能，提供基本欄位，如用戶名、密碼、電郵、群組與權限
# from django.contrib.auth.models import User
# (原本是使用User的，但我想擴展User模型新增role欄位，所以我在models.py中建立了CustomUser，其有User的所有欄位與功能)
from .models import CustomUser, UserRole

# serializers將Django模型(或資料)轉換成JSON格式，並進行反向轉換(JSON轉模型實例)的工具，同時也對資料進行驗證，確保客戶端發送的資料符合格式與要求
from rest_framework import serializers
import logging #偵錯

logger = logging.getLogger("api")

class UserSerializer(serializers.ModelSerializer):
    # ModelSerializer是DRF的模型序列化器，將 Django 模型（Model） 轉換為 JSON，並且處理 JSON 到 模型實例 的轉換

    role = serializers.ChoiceField(
        choices=UserRole.choices, default=UserRole.WAREHOUSE
    )  # 使role欄位只能接受事先定義好的選項(UserRole的選項)

    class Meta:  # 是ModelSerializer的類別之一，用來定義與ModelSerializer 關聯的模型(model) 以及需要序列化的欄位(field)。
        model = CustomUser
        fields = ["id", "username", "password", "last_login", "role"]
        extra_kwargs = {
            "password": {"write_only": True}
        }  # 為password欄位增加額外屬性（write_only只能在request時寫入，不會在API response時回傳），這樣回傳的JSON檔案會排除password欄位
        # 這代表用戶透過API傳入密碼給後端資料庫儲存，但API不能從資料庫讀取密碼

    def validate(self, data):
        """
        檢查使用者名稱與密碼是否有空值
        """
        try:
            if not data.get("username"):
                raise serializers.ValidationError("username field cannot be empty")
            if not data.get("password"):
                raise serializers.ValidationError("password field cannot be empty")
        except Exception as e:
            logger.error("使用者名稱與密碼資料檢查空值時發生錯誤: %s", str(e), exc_info=True)
        return data
    
    def validate_username(self, value): 
        """
        檢查username是否已經儲存在資料庫
        """
        if CustomUser.objects.filter(username = value).exists(): #將取得的資料過濾資料庫內的username，有結果則使用者已經存在
            raise serializers.ValidationError("Username already exists")
        return value

    def create(self, validated_data):
        """
        函數目標：自訂物件的建立方式，確保資料安全並正確存入資料庫
        1. 所有經過序列化器驗證過的資料，尤其是密碼會被create_user()自動加密存入資料庫，相較ModelSerializer預設使用User.object.create()，這樣create()仍會儲存到明文密碼到資料庫
        2. 能為未來擴充資料處理邏輯，如新增預設值（註冊便自動給一個預設角色）、新增email欄位、觸發額外動作（email驗證）
            如user.profile.role = "user
        validated_data代表驗證過的資料，但若沒有自定義驗證，只是驗證輸入的資料是否符合當初設定fields的資料類型規則，如max_length、EmailField驗證原始資料是否是Email格式
            就算資料是空值仍會視為驗證過
        """
        try:
            # # is_staff(bool)表示用戶是否可以登入管理後台，用pop()移除此key，如果validated_data字典中沒有名為is_staff的key，則返回預設值None。避免駭客藉由API修改自己的帳號權限
            is_staff = validated_data.get("is_staff", False) 
            # # is_superuser表示用戶是否擁有所有權限，同理
            is_superuser = validated_data.get("is_superuser", False)

            user = CustomUser.objects.create_user(
                username=validated_data["username"],
                password=validated_data["password"],
                last_login=validated_data.get("last_login"),
                role=validated_data.get("role", UserRole.WAREHOUSE),# 從validated_data字典中取得key為 role 的值，如果不存在key為role的值則預設Warehouse
                is_staff=is_staff,
                is_superuser=is_superuser,
            )
        except Exception as e:
            print(f"Error data: {validated_data}")
            logger.error("建立並傳送使用者資料到資料庫時發生錯誤: %s", str(e), exc_info=True)
            raise serializers.ValidationError("使用者創建失敗")
        return user
