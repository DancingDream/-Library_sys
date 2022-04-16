<template>
	<view class="container">
		<view class="banner">
			<view class="userinfo">
				<u-avatar size="110"></u-avatar>
				<view class="leftInfo">
					<view class="username">

						<text class="" v-if="state">{{this.userInfo.nickName}}</text>
						<text class="" v-else>未登录</text>
					</view>
					<view class="tip">
						<text>编辑个性化签名</text>
					</view>
				</view>
				<view class="btn">
					<u-button @click="edit"
						style="font-size: 13px;background-color: #0045d0;color: #ffffff;border: none;opacity: 0.9;"
						:hair-line="false" shape="circle">编辑个人资料</u-button>
				</view>
			</view>
		</view>
		<view class="notice">
			<view class="notB">
				<text>系统通知：请完善个人信息！</text>
			</view>
		</view>

		<view class="appList">
			<view class="app_item">
				<view class="app_item_1" @click="record">
					<u-image width="80rpx" height="80rpx" src="/static/img/book.png"></u-image>
					<text style="margin-top: 8rpx;">借书记录</text>
				</view>
			</view>
		</view>

		<view class="logout">
			<u-button @click="logout" type="primary" style="box-shadow: 1px 5px 10px #a5ceff;" shape="circle"
				v-if="state">退出登录</u-button>
			<u-button @click="login" type="primary" style="box-shadow: 1px 5px 10px #a5ceff;" shape="circle" v-else>登录
			</u-button>
		</view>
	</view>
</template>

<script>
	import {
		getUserInfo,
		exit
	} from "../../common/api.js"
	import store from "../../store"

	export default {
		data() {
			return {
				userInfo: {

				},
				state: false,
			}
		},
		methods: {

			initInfo() {
				this.userInfo = {};
				console.log(store.state.token);
				getUserInfo(store.state.token).then((res) => {
					this.userInfo = res.data;
					console.log(this.userInfo);
					console.log(res.data);
				});
				if (this.userInfo === null) {
					this.state = false;
				} else {
					this.state = true;
				}
				if (this.userInfo.banState) {
					uni.showToast({
						title: '该账号已被禁用，请联系管理员解禁',
						icon: 'error',
						duration: 5000,
						
					})
				}
			},

			edit() {
				uni.navigateTo({
					url: '../userinfo/userinfo'
				})
			},
			record() {
				uni.navigateTo({
					url: '../borrowingRecord/borrowingRecord'
				})
			},

			login() {
				uni.reLaunch({
					url: '../login/login'
				})
			},

			logout() {
				exit(store.state.token).then(() => {
					store.commit("clearToken");
					sessionStorage.clear();
					this.state = false;
					this.initInfo()
				})
			}
		},

		mounted() {
			this.initInfo();

		}

	}
</script>

<style scoped lang="scss">
	page {
		background-color: #eee;
	}

	.container {
		.warningBanState {
			display: flex;
		}

		.banner {
			padding: 40rpx;
			height: 375rpx;
			background-color: #0055ff;
			display: flex;
			align-items: center;
			position: relative;
			z-index: 1;

			.userinfo {
				margin-left: 10rpx;
				display: flex;
				align-items: center;

				.leftInfo {
					margin-left: 40rpx;
					font-size: 20px;
					color: #FFFFFF;

					.username {

						// font-weight: 700;
					}

					.tip {
						font-size: 14px;
						// color: #888888;
					}
				}

				.btn {
					position: absolute;
					right: 5%;
				}
			}
		}

		.notice {
			height: 100rpx;
			margin-top: -50rpx;
			padding: 0 20rpx;
			position: relative;
			z-index: 2;

			.notB {
				display: flex;
				border-radius: 12rpx;
				background-color: #FFFFFF;
				height: 100%;
				color: #e74d73;
				font-weight: 700;
				align-items: center;
				padding: 0 20rpx;
			}
		}

		.appList {
			padding: 20rpx;
			margin-top: 20rpx;

			.app_item {
				background-color: #FFFFFF;
				border-radius: 12rpx;
				padding: 40rpx;

				.app_item_1 {
					display: flex;
					flex-direction: column;
					justify-content: center;
					align-items: center;
					width: 150rpx;
				}
			}
		}

		.logout {
			width: 100%;
			padding: 0 80rpx;
			position: absolute;
			bottom: 5%;

		}
	}
</style>
