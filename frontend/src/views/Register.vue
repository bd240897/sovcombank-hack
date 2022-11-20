<template>

<section class="login h-100">
    <div class="container d-flex flex-column h-100">

        <div class="snowflake h-25 mb-2">

        </div>

        <div class="block">
            <div class="login__header text-center mx-0 px-0">
                ПРОСТРАНСТВО ВОЗМОЖНОСТЕЙ
            </div>

            <div class="login__form w-100">
                <div class="form__email form-group my-4">
                    <input class="form__password__item form-control" type="email" id="exampleInputEmail1"
                           aria-describedby="emailHelp" placeholder="Логин">
                </div>

                <div class="form__password form-group my-4">
                    <input class="form__password__item form-control" type="password" id="exampleInputPassword1"
                           placeholder="Пароль">
                </div>

                <div class="form__password_repeat form-group my-4">
                    <input class="form__password__item form-control" type="password" id="exampleInputPassword2"
                           placeholder="Пароль">
                </div>

                <div class="login__button">
                    <button class="button_item btn btn-primary w-100" type="submit">Зарегистрироваться</button>
                </div>
            </div>
        </div>

    </div>
</section>

</template>

<script>
import goToSomewhere from "@/mixins/goToSomewhere";

export default {
  name: "Register",
  mixins: [goToSomewhere],
}
</script>

<style scoped>

    @import url('https://fonts.googleapis.com/css2?family=Oswald&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Cabin:wght@700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Rubik:wght@600&display=swap');

    html, body {
        height: 100%;
    }

    .login {
        background: linear-gradient(180deg, #25055A 0%, #57254E 60.73%, #E07D2F 75.83%);
    }


    .login__header {
        font-family: Cabin, serif;
        font-weight: 700;
        color: white;
        font-size: 32px;
    }

    .form__password_repeat{
        padding-bottom: 60px;
    }


    .form__password__item {
        border-radius: 20px;
        border: 2px solid #5c636a;
    }


    .login__button {

    }

    .button_item {
        /* фон */
        background-color: white;
        border-radius: 15px;
        border: 2px solid #5c636a;

        /* тексt */
        font-size: 32px;
        font-family: Rubik, sans-serif;
        font-weight: 600;
        color: black;
    }

    .snowflake {
          background: url(../assets/img/group_18.png);
    }

</style>