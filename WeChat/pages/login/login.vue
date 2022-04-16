<template>
	<view class="container">
		<view class="banner">
			<text>欢迎登录</text>
			<image src="../../static/user/banner.png" mode=""></image>
		</view>

		<view class="login_box">
			<view class="box">
				<view class="box_title">
					<text>账号登录</text>
					<view class="bar">

					</view>
				</view>

				<view class="box_input">
					<!-- <u-form :model="loginForm" ref="loginForm" class="box_input">
						<u-form-item label="用户账号" label-position="top" prop="userID" class="input_user">
							<input type="text" value="" placeholder="请输入账号/手机号/电子邮箱" placeholder-class="userInputplaceholder" v-model="loginForm.userID" />
						</u-form-item>
						
						<u-form-item label="用户账号" label-position="top" prop="passWord" class="input_psw">
							<input type="password" value="" placeholder="请输入密码" placeholder-class="userInputplaceholder" v-model="loginForm.passWord" />
						</u-form-item>
						
					</u-form> -->

					<view class="input_user">
						<input type="text" value="" placeholder="请输入账号/手机号/电子邮箱"
							placeholder-class="userInputplaceholder" v-model="loginForm.userID" />
					</view>

					<view class="input_psw">
						<input type="password" value="" placeholder="请输入密码" placeholder-class="userInputplaceholder"
							v-model="loginForm.passWord" />
					</view>
				</view>

				<view class="btn_box">
					<button @click="Onlogin" class="btnCla "
						style="background-color: #79b2fe;color: #FFFFFF;font-weight: 700;">登录</button>
				</view>

				<view class="goReg">
					<navigator url="../register/register"><text>暂无账号?去注册</text></navigator>
				</view>

			</view>


		</view>
	</view>
</template>

<script>
	import {
		login
	} from "../../common/api.js";
	import {
		MD5
	} from "../../js/MD5.js";
	import store from "../../store";


	export default {
		data() {
			return {
				loginForm: {
					userID: '',
					passWord: ''
				},
			}
		},
		methods: {
			Onlogin() {
				if (this.loginForm.userID === '' || this.loginForm.passWord === '') {
					uni.showToast({
						title: '请正确输入信息',
						icon: 'error',
					});
				} else {
					uni.showLoading({
						title: '正在登录',
					});
					this.loginForm.MD5passWord = MD5(this.loginForm.passWord);
					this.loginForm.passWord = '';
					login(this.loginForm).then(res => {
						store.commit('setToken', res.data.token);
						sessionStorage.setItem("token", res.data.token);

						uni.showToast({
							title: '登录成功'
						});

						uni.switchTab({
							url: '../index/index'
						});



					})



				}




			}
		}
	}
</script>

<style scoped lang="scss">
	.container {

		.banner {
			position: relative;
			height: 680rpx;

			text {
				position: absolute;
				top: 25%;
				left: 8%;
				font-size: 60rpx;
				font-weight: 700;
				color: #ffffff;
			}

			image {
				position: absolute;
				z-index: -1;
				width: 750rpx;
				height: 675rpx;
			}
		}

		.login_box {
			padding: 40rpx;

			.box {
				margin-top: -220rpx;
				padding: 40rpx;
				// height: 635rpx;
				border: .5px solid #e7f0fb;
				background-color: #ffffff;
				border-radius: 40rpx;
				box-shadow: 1px 2px 10px #eeeeee;

				.box_title {
					display: flex;
					flex-direction: column;
					justify-content: center;
					align-items: center;
					color: #1578fe;
					font-weight: 700;

					.bar {
						margin-top: 8rpx;
						width: 26rpx;
						height: 8rpx;
						background-color: #1678fd;
						border-radius: 8rpx;
					}
				}

				.box_input {

					padding: 10rpx 15rpx;

					.input_user {
						margin-top: 40rpx;
						padding: 0 40rpx;
						height: 85rpx;
						background-color: #deecff;
						border-radius: 18rpx;

						input {
							height: 100%;
						}

						.userInputplaceholder {
							color: #70a5ed;
							font-weight: 700;
						}
					}

					.input_psw {
						margin-top: 40rpx;
						padding: 0 40rpx;
						height: 85rpx;
						background-color: #deecff;
						border-radius: 18rpx;

						input {
							height: 100%;
						}

						.userInputplaceholder {
							color: #70a5ed;
							font-weight: 700;
						}
					}

				}

				.btn_box {
					margin-top: 30rpx;
					padding: 10rpx 15rpx;

					.btnCla {
						background-color: #79b2fe !important;
						font-weight: 700;
						padding: 0 20rpx;
					}

					.btnCla::after {}

					.btnCla::after {
						content: ' ';
						position: absolute;
						pointer-events: none;
						// 设置为border-box，意味着下面的scale缩小为0.5，实际上缩小的是伪元素的内容（border-box意味着内容不含border）
						box-sizing: border-box;
						// 中心点作为变形(scale())的原点
						-webkit-transform-origin: 0 0;
						transform-origin: 0 0;
						left: 0;
						top: 0;
						width: 199.8%;
						height: 199.7%;
						-webkit-transform: scale(0.5, 0.5);
						transform: scale(0.5, 0.5);
						border: 1px solid currentColor;
						z-index: 1;
					}

					.u-wave-ripple {
						z-index: 0;
						position: absolute;
						border-radius: 100%;
						background-clip: padding-box;
						pointer-events: none;
						user-select: none;
						transform: scale(0);
						opacity: 1;
						transform-origin: center;
					}
				}

				.goReg {
					padding: 20rpx;
					color: #658fc1;
					font-size: 14px;
				}
			}
		}
	}
</style>
