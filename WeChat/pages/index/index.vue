<template>
	<view class="container">
		<u-navbar :is-back="false">
			<view class="nav_icon">
				<view class="">
					<u-icon size="35" name="search"></u-icon>
				</view>
				<view class="">
					<u-icon size="35" name="scan"></u-icon>
				</view>

			</view>
		</u-navbar>

		<view class="banner_info">
			<view class="box_title_big">
				<text>书读百遍，其义自见</text>
			</view>
			<view class="box_title_mini">
				<text>一杯咖啡，一本书，一位朋友</text>
			</view>
		</view>

		<ul class="book_list" v-for="(item,index) in activeinHouseList" :key="index">
			<li class="book_item">
				<view class="book_pic">
					<view class="pic">
						<u-image :src='item.cover' width="100%" height="100%" mode="scaleToFill"></u-image>
					</view>
					<view class="pic_info">
						<view class="book_name">
							<text>{{item.bookName}}</text>
						</view>
						<view class="book_info_tip">
							<text>{{item.author}}</text>
						</view>
						<view class="book_info_cb">
							<text><span>{{item.pubLisher}}</span>/<span>{{item.pubDate}}</span></text>
						</view>
					</view>
				</view>
				<view class="book_info">
					<text class="book_type">{{item.category}}</text>
					<!-- 					<view class="mark">
						<u-icon size="35" name="star" ></u-icon>
						<text class="star_num">10</text>
					</view> -->
				</view>
			</li>
		</ul>


	</view>
</template>

<script>
	import {
		getBooks
	} from "../../common/api.js"

	export default {


		data() {
			return {
				booksForm: [],
				dataList: "",
			}
		},
		onLoad() {

		},
		methods: {

			//初始化书本信息
			initBooksForm() {
				this.booksForm = [];
				this.activeinHouseList = [];
				getBooks().then(res => {
					this.booksForm = res.data;
					console.log(this.booksForm);
				})
				this.dataList = this.booksForm;

			}
		},

		computed: {
			activeinHouseList: function() {
				return this.booksForm.filter((item) => {
					return item.state == true;
				})
			}
		},

		mounted() {
			this.initBooksForm();
			console.log(this.booksForm);
		}
	}
</script>

<style scoped lang="scss">
	ul,
	ol,
	li {
		list-style: none;
	}

	.container {
		padding: 40rpx;

		.nav_icon {
			padding: 40rpx;

			view {
				display: inline-block;
				margin-right: 25rpx;
			}
		}

		.banner_info {
			margin-bottom: 80rpx;

			.box_title_big {
				font-weight: 700;
				font-size: 20px;
			}

			.box_title_mini {
				margin-top: 5rpx;
				font-size: 13px;
				color: rgb(122, 126, 131);
			}
		}

		.book_list {
			margin-bottom: 20rpx;
			padding: 5rpx;

			.book_item {
				// background-color: #007AFF;
				border-radius: 10rpx;
				box-shadow: 2px 3px 10px #e5e5e5;
				height: 347rpx;

				.book_pic {
					border-radius: 10rpx 10rpx 0 0;
					height: 257rpx;
					background-color: #626262;
					display: flex;

					.pic {
						width: 200rpx;
						padding: 10rpx 0;
						margin-left: 20rpx;

					}

					.pic_info {
						margin-left: 40rpx;
						margin-top: 40rpx;

						.book_name {
							color: #FFFFFF;
							font-weight: 700;
							font-size: 16px;
						}

						.book_info_tip {
							margin-top: 10rpx;
							color: #d3d3d3;
							font-size: 12px;
						}

						.book_info_cb {
							color: #d3d3d3;
							// margin-top: 5rpx;
							font-size: 12px;
						}
					}
				}

				.book_info {

					display: flex;
					align-items: center;
					// justify-content: center;
					height: 100rpx;
					position: relative;

					.book_type {
						margin-left: 40rpx;
						font-weight: 700;
					}

					.mark {
						display: flex;
						align-items: center;
						position: absolute;
						right: 5%;

						.star_num {
							margin-left: 10rpx;
						}
					}

				}
			}
		}
	}
</style>
